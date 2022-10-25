from odoo import api, models, http
from odoo.http import request


class Website(models.Model):
    _inherit = 'website'
    
    def _get_theme(self):
        """
        This method to get all modules whose name starts with "theme" in addon path
        """
        themes = []
        domain = [('name', '=like', 'theme%'), ('name', 'not in', [
            'theme_default']), ('state', '!=', 'uninstallable')]
        themes_name = http.request.env['ir.module.module'].search(domain).mapped('name')
        for theme_name in themes_name:
            themes.append({
                'name': theme_name
            })
        return themes
    
    def _get_theme_id(self, theme_name):
        """
        This method to get the ID of the theme in the table ir.module.module, 
        used to determine the id of the industry to be selected
        """
        domain = [('name', '=', theme_name)]
        theme_id = self.env['ir.module.module'].search(domain, limit=1).mapped('id')[0]
        return theme_id
        
    def _get_industry_id(self, theme_name):
        """
        returns a list of labels of themes, used to fill in the industry selection box. 
        The value depends on the keywords in the key industries of each theme
        """
        summary_list = http.addons_manifest[theme_name].get('industries', [])       
        if summary_list:
            label_list = summary_list.split(',')              
            return label_list

    def _get_image_urls(self, theme_name):
        """
        This method is used to get the image in the module instead of the image on the odoo api.
        These images are used to display in the theme preview mode (the second step or the configurator_recommended_themes function) 
        It will rely on the key images_preview_theme in the manifest. 
        In which there will be value pairs website.snippetsname_url: image path
        """
        image_urls = {}
        if theme_name:           
            client_theme_img = http.addons_manifest[theme_name].get('images_preview_theme', {})
            for image_key, url in client_theme_img.items():
                image_urls.update({
                    '%s_url' % (image_key.replace('website.', '#')): url,
                })
        return image_urls
    
    def _get_images(self, theme_name):
        """
        This method will return the image, to be used in the web page. 
        It will get the images in the module instead of on the odoo api, 
        We will process the string here to match the key: value pair format of the images_preview_theme key 
        in the manifest of each theme module.
        These images will be used in the last step (or do configurator_apply )
        """
        images = http.addons_manifest[theme_name].get('images_preview_theme', {})
        return images
    
    def _change_images(self, images):
        """
        This method is used to change the path and type of the image after it is called from the odoo api
        param: 1 dict consisting of many pairs of "image name : image path" value pairs
            eg: "website.s_cover_default_image":"your_image_url_path"
        return: 1 new dict with old keys and new path
        """
        for name, url in images.items():
            domain = [('website_id', '=', self.get_current_website().id), ('name', '=', name)]
            self.env['ir.attachment'].search(domain).write({
                'url': url,
                'type': 'url'
            })
    
    @api.model
    def configurator_init(self):
        """
        This method will change the selection from the professions on the odoo api to the synonym of the theme modules,
        based on the module's summary in each theme's manifest.
        return: returns 1 dict pair of value pairs. 3 keys include:
            features
            logo
            industries
        """
        res = super().configurator_init()
        res['industries'] = []
        themes = self._get_theme()
        if themes:
            themes_name = [theme.get('name') for theme in themes]
            for theme_name in themes_name:
                industry_id = self._get_theme_id(theme_name)
                industry_list = self._get_industry_id(theme_name)
                for industry in industry_list:
                    industry_label = industry.strip()
                    res['industries'].append({
                        'id': industry_id,
                        'label': industry_label,
                        'Synonyms': False
                    })
        return res

    @api.model
    def configurator_recommended_themes(self, industry_id, palette):
        """
        param 1: industry_id: selected in step configurator/2
        param 2: palette: color for web page, selected in step configurator/3
        return: 1 list of 3 themes, each theme has value pairs "additional name: processed svg file"
            layout: file SVG in random theme module, based on theme ID arrangement in models ir.module.module
            images: rely on industry parameter to return image in preview mode
        This method is used to display the web page in preview mode. 
        Will take the images in the module to insert into the address in the corresponding SVG file
        """
        res = super().configurator_recommended_themes(industry_id, palette)
        theme_name_for_industry = request.env['ir.module.module'].search([('id', '=', industry_id)])
        if theme_name_for_industry:
            theme_name_industry = theme_name_for_industry.mapped('name')[0]
        for theme in res:
            theme['image_urls'] = self._get_image_urls(theme_name_industry)
            theme['svg'] = False      
        process_svg = self.env['website.configurator.feature']._process_svg
        for theme in res:
            theme['svg'] = process_svg(theme['name'], palette, theme.pop('image_urls'))
        return res

    @api.model
    def configurator_apply(self, **kwargs):
        """
        This method is used to configure the options in the previous steps, returning a complete web page. 
        It will take the layout as an SVG file, configure the snippets in step 2 selection ( configurator_recommended_themes function ), 
        images based on the industry selection in step 1 ( configurator_init )
        param: **kwargs: includes the values selected in the previous steps. color, industry, logo, theme name, features..
        return: return 1 action, do 1 action to build the site with the parameters after configuration
        """
        res = super(Website, self).configurator_apply(**kwargs)
        custom_resources = {}
        industry_id = kwargs['industry_id']
        theme_name_for_industry = request.env['ir.module.module'].search([('id', '=', industry_id)])
        if theme_name_for_industry:
            theme_name_for_industry_id = theme_name_for_industry.mapped('name')[0]
            custom_resources['images'] = self._get_images(theme_name_for_industry_id)
            images = custom_resources.get('images', {}) 
            self._change_images(images)
        return res
