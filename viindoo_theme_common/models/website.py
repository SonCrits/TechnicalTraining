import json
import logging
import requests

from lxml import etree, html


from odoo import api, models, registry, http

from odoo.http import request
from odoo.tools.translate import _
from odoo.tools import pycompat

logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = 'website'
    
    @api.model
    def _get_viindoo_theme(self):
        themes = []
        domain = [('name', '=like', 'theme_viin%'), ('name', 'not in', [
            'theme_default', 'theme_common']), ('state', '!=', 'uninstallable')]
        themes_name = http.request.env['ir.module.module'].search(domain).mapped('name')
        for theme_name in themes_name:
            themes.append({
                'name': theme_name
            })
        return themes
    
    @api.model
    def _get_theme_id(self, theme_name):
        domain = [('name', '=', theme_name)]
        theme_viindoo_id = self.env['ir.module.module'].search(domain, limit=1).mapped('id')[0]
        return theme_viindoo_id
        
    @api.model
    def _get_industry_id(self, theme_name):
        label = http.addons_manifest[theme_name].get('name', [])
        return label

    @api.model
    def _get_image_urls(self, theme_name):
        image_urls = {}
        client_theme_img = http.addons_manifest[theme_name].get('images_preview_theme', {})
        for image_key, url in client_theme_img.items():
            image_urls.update({
                '%s_url' % (image_key.replace('website.', '#')): url,
            })
        return image_urls
    
    @api.model
    def _get_images(self, theme_name):
        images = {}
        client_theme_img = http.addons_manifest[theme_name].get('images_preview_theme', {})
        for image_key, url in client_theme_img.items():
            images.update({
                '%s' % (image_key.replace('website.', '')): url,
            })
        return images
    
    @api.model
    def configurator_init(self):
        r = dict()
        company = self.get_current_website().company_id
        configurator_features = self.env['website.configurator.feature'].with_context(lang=self.get_current_website().default_lang_id.code).search([])
        r['features'] = [{
            'id': feature.id,
            'name': feature.name,
            'description': feature.description,
            'type': 'page' if feature.page_view_id else 'app',
            'icon': feature.icon,
            'website_config_preselection': feature.website_config_preselection,
            'module_state': feature.module_id.state,
        } for feature in configurator_features]
        r['logo'] = False
        if company.logo and company.logo != company._get_logo():
            r['logo'] = company.logo.decode('utf-8')
        themes = self._get_viindoo_theme()
        themes_name = [theme.get('name') for theme in themes]
        r['industries'] = [{
            'id': self._get_theme_id(theme_name),
            'label': self._get_industry_id(theme_name),
            'Synonyms': False
        } for theme_name in themes_name]
        return r

    @api.model
    def configurator_recommended_themes(self, industry_id, palette):
        themes = self._get_viindoo_theme()
        themes_name = [theme.get('name') for theme in themes]
        theme_name_for_industry_id = request.env['ir.module.module'].search([('id', '=', industry_id)]).mapped('name')[0]
        themes_suggested = list({
            'name': theme_name,                                                                                                                                              
            'image_urls': self._get_image_urls(theme_name_for_industry_id)
        }for theme_name in themes_name)
        process_svg = self.env['website.configurator.feature']._process_svg
        for theme in themes_suggested:
            theme['svg'] = process_svg(theme['name'], palette, theme.pop('image_urls'))
        return themes_suggested
    
    @api.model
    def configurator_apply(self, **kwargs):
        def set_colors(selected_palette):
            url = '/website/static/src/scss/options/user_values.scss'
            selected_palette_name = selected_palette if isinstance(selected_palette, str) else 'base-1'
            values = {'color-palettes-name': "'%s'" % selected_palette_name}
            self.env['web_editor.assets'].make_scss_customization(url, values)

            if isinstance(selected_palette, list):
                url = '/website/static/src/scss/options/colors/user_color_palette.scss'
                values = {f'o-color-{i}': color for i, color in enumerate(selected_palette, 1)}
                self.env['web_editor.assets'].make_scss_customization(url, values)

        def set_features(selected_features):
            features = self.env['website.configurator.feature'].browse(selected_features)

            menu_company = self.env['website.menu']
            if len(features.filtered('menu_sequence')) > 5 and len(features.filtered('menu_company')) > 1:
                menu_company = self.env['website.menu'].create({
                    'name': _('Company'),
                    'parent_id': website.menu_id.id,
                    'website_id': website.id,
                    'sequence': 40,
                })

            pages_views = {}
            modules = self.env['ir.module.module']
            module_data = {}
            for feature in features:
                add_menu = bool(feature.menu_sequence)
                if feature.module_id:
                    if feature.module_id.state != 'installed':
                        modules += feature.module_id
                    if add_menu:
                        if feature.module_id.name != 'website_blog':
                            module_data[feature.feature_url] = {'sequence': feature.menu_sequence}
                        else:
                            blogs = module_data.setdefault('#blog', [])
                            blogs.append({'name': feature.name, 'sequence': feature.menu_sequence})
                elif feature.page_view_id:
                    result = self.env['website'].new_page(
                        name=feature.name,
                        add_menu=add_menu,
                        page_values=dict(url=feature.feature_url, is_published=True),
                        menu_values=add_menu and {
                            'url': feature.feature_url,
                            'sequence': feature.menu_sequence,
                            'parent_id': feature.menu_company and menu_company.id or website.menu_id.id,
                        },
                        template=feature.page_view_id.key
                    )
                    pages_views[feature.iap_page_code] = result['view_id']

            if modules:
                modules.button_immediate_install()
                assert self.env.registry is registry()

            self.env['website'].browse(website.id).configurator_set_menu_links(menu_company, module_data)

            return pages_views

        def configure_page(page_code, snippet_list, pages_views, cta_data):
            if page_code == 'homepage':
                page_view_id = website.homepage_id.view_id
            else:
                page_view_id = self.env['ir.ui.view'].browse(pages_views[page_code])
            rendered_snippets = []
            nb_snippets = len(snippet_list)
            for i, snippet in enumerate(snippet_list, start=1):
                try:
                    view_id = self.env['website'].with_context(website_id=website.id, lang=website.default_lang_id.code).viewref('website.' + snippet)
                    if view_id:
                        el = html.fromstring(view_id._render(values=cta_data))

                        # Add the data-snippet attribute to identify the snippet
                        # for compatibility code
                        el.attrib['data-snippet'] = snippet

                        # Tweak the shape of the first snippet to connect it
                        # properly with the header color in some themes
                        if i == 1:
                            shape_el = el.xpath("//*[hasclass('o_we_shape')]")
                            if shape_el:
                                shape_el[0].attrib['class'] += ' o_header_extra_shape_mapping'

                        # Tweak the shape of the last snippet to connect it
                        # properly with the footer color in some themes
                        if i == nb_snippets:
                            shape_el = el.xpath("//*[hasclass('o_we_shape')]")
                            if shape_el:
                                shape_el[0].attrib['class'] += ' o_footer_extra_shape_mapping'
                        rendered_snippet = pycompat.to_text(etree.tostring(el))
                        rendered_snippets.append(rendered_snippet)
                except ValueError as e:
                    logger.warning(e)
            page_view_id.save(value=''.join(rendered_snippets), xpath="(//div[hasclass('oe_structure')])[last()]")

        def set_images(images):
            for name, url in images.items():
                try:
                    response = requests.get(url, timeout=3)
                    response.raise_for_status()
                except Exception as e:
                    logger.warning("Failed to download image: %s.\n%s", url, e)
                else:
                    attachment = self.env['ir.attachment'].create({
                        'name': name,
                        'website_id': website.id,
                        'key': name,
                        'type': 'binary',
                        'raw': response.content,
                        'public': True,
                    })
                    self.env['ir.model.data'].create({
                        'name': 'configurator_%s_%s' % (website.id, name.split('.')[1]),
                        'module': 'website',
                        'model': 'ir.attachment',
                        'res_id': attachment.id,
                        'noupdate': True,
                    })

        website = self.get_current_website()
        theme_name = kwargs['theme_name']
        theme = self.env['ir.module.module'].search([('name', '=', theme_name)])
        url = theme.button_choose_theme()

        # Force to refresh env after install of module
        assert self.env.registry is registry()

        website.configurator_done = True

        # Enable tour
        tour_asset_id = self.env.ref('website.configurator_tour')
        tour_asset_id.copy({'key': tour_asset_id.key, 'website_id': website.id, 'active': True})

        # Set logo from generated attachment or from company's logo
        logo_attachment_id = kwargs.get('logo_attachment_id')
        company = website.company_id
        if logo_attachment_id:
            attachment = self.env['ir.attachment'].browse(logo_attachment_id)
            attachment.write({
                'res_model': 'website',
                'res_field': 'logo',
                'res_id': website.id,
            })
        elif not logo_attachment_id and company.logo and company.logo != company._get_logo():
            website.logo = company.logo.decode('utf-8')

        # palette
        palette = kwargs.get('selected_palette')
        if palette:
            set_colors(palette)

        # Update CTA
        cta_data = website.get_cta_data(kwargs.get('website_purpose'), kwargs.get('website_type'))
        if cta_data['cta_btn_text']:
            xpath_view = 'website.snippets'
            parent_view = self.env['website'].with_context(website_id=website.id).viewref(xpath_view)
            self.env['ir.ui.view'].create({
                'name': parent_view.key + ' CTA',
                'key': parent_view.key + "_cta",
                'inherit_id': parent_view.id,
                'website_id': website.id,
                'type': 'qweb',
                'priority': 32,
                'arch_db': """
                    <data>
                        <xpath expr="//t[@t-set='cta_btn_href']" position="replace">
                            <t t-set="cta_btn_href">%s</t>
                        </xpath>
                        <xpath expr="//t[@t-set='cta_btn_text']" position="replace">
                            <t t-set="cta_btn_text">%s</t>
                        </xpath>
                    </data>
                """ % (cta_data['cta_btn_href'], cta_data['cta_btn_text'])
            })
            try:
                view_id = self.env['website'].viewref('website.header_call_to_action')
                if view_id:
                    el = etree.fromstring(view_id.arch_db)
                    btn_cta_el = el.xpath("//a[hasclass('btn_cta')]")
                    if btn_cta_el:
                        btn_cta_el[0].attrib['href'] = cta_data['cta_btn_href']
                        btn_cta_el[0].text = cta_data['cta_btn_text']
                    view_id.with_context(website_id=website.id).write({'arch_db': etree.tostring(el)})
            except ValueError as e:
                logger.warning(e)

        # modules
        pages_views = set_features(kwargs.get('selected_features'))
        # We need to refresh the environment of website because set_features installed some new module
        # and we need the overrides of these new menus e.g. for .get_cta_data()
        website = self.env['website'].browse(website.id)

        # Update footers links, needs to be done after `set_features` to go
        # through module overide of `configurator_get_footer_links`
        footer_links = website.configurator_get_footer_links()
        footer_ids = [
            'website.template_footer_contact', 'website.template_footer_headline',
            'website.footer_custom', 'website.template_footer_links',
            'website.template_footer_minimalist',
        ]
        for footer_id in footer_ids:
            try:
                view_id = self.env['website'].viewref(footer_id)
                if view_id:
                    # Deliberately hardcode dynamic code inside the view arch,
                    # it will be transformed into static nodes after a save/edit
                    # thanks to the t-ignore in parents node.
                    arch_string = etree.fromstring(view_id.arch_db)
                    el = arch_string.xpath("//t[@t-set='configurator_footer_links']")[0]
                    el.attrib['t-value'] = json.dumps(footer_links)
                    view_id.with_context(website_id=website.id).write({'arch_db': etree.tostring(arch_string)})
            except Exception as e:
                # The xml view could have been modified in the backend, we don't
                # want the xpath error to break the configurator feature
                logger.warning(e)

        # Load suggestion from iap for selected pages
        custom_resources = {}
        industry_id = kwargs['industry_id']
        theme_name_for_industry_id = request.env['ir.module.module'].search([('id', '=', industry_id)]).mapped('name')[0]
        custom_resources['images'] = self._get_images(theme_name_for_industry_id)

        # Update pages
        requested_pages = list(pages_views.keys()) + ['homepage']
        snippet_lists = website.get_theme_snippet_lists(theme_name)
        for page_code in requested_pages:
            configure_page(page_code, snippet_lists.get(page_code, []), pages_views, cta_data)

        images = custom_resources.get('images', {})
        set_images(images)
        return url
