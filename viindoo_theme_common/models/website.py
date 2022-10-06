from odoo import models, api, http
from odoo.http import request



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
        res = super(Website, self).configurator_init()

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


    
