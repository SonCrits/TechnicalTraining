from odoo import models, api, http


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def configurator_recommended_themes(self, industry_id, palette):
        viindoo_them = self._get_viindoo_theme(industry_id)
        process_svg = self.env['website.configurator.feature']._process_svg
        for theme in viindoo_them:
            theme['svg'] = process_svg(theme['name'], palette, theme.pop('image_urls'))
        return viindoo_them

    def _get_viindoo_theme(self, industry_id):
        """
        This method will search all Viindoo themes whose name starts with theme_viin
        Returns at most 3 themes with industrys matching industry_id
        """
        themes = []
        domain = [('name', '=like', 'theme_viin%'), ('name', 'not in', [
            'theme_default', 'theme_common']), ('state', '!=', 'uninstallable')]
        themes_name = http.request.env['ir.module.module'].search(domain).mapped('name')

        # Only up to 3 themes
        themes_name = list(filter(lambda theme_name: industry_id in self._get_theme_category(
            theme_name), themes_name))[:3]
        for theme_name in themes_name:
            themes.append({
                'name': theme_name,
                'image_urls': self._get_image_urls(theme_name),
            })
        return themes

    @api.model
    def _get_theme_category(self, theme_name):
        """
        This method looks in the manifest for the_category field and returns its value.
        theme_category: [1, 2, 3], it is a list of industries
        """
        return http.addons_manifest[theme_name].get('theme_category', [])

    @api.model
    def _get_image_urls(self, theme_name):
        """
        This method will format images_preview_theme to standard dictionary form of Odoo
        images_preview_theme has the form {'website.image_name':url}
        will return image_urls has the form {'#image_name_url':url}
        image_urls is used to replace the id of the image in the .svg file
        """
        image_urls = {}
        client_theme_img = http.addons_manifest[theme_name].get('images_preview_theme', {})
        for image_key, url in client_theme_img.items():
            image_urls.update({
                '%s_url' % (image_key.replace('website.', '#')): url,
            })
        return image_urls
