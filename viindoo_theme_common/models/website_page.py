from odoo import models, fields, api


class Page(models.Model):
    _inherit = 'website.page'

    is_header_absolute = fields.Boolean(string='Header Transparent', default=False, help="Make header transparent on this page")

    def check_absolute_header(self):
        return 'transparent_header ' if self.is_header_absolute else ''

    @api.model
    def save_page_info(self, website_id, data):
        page = self.browse(int(data['id']))
        vals = {
            'is_header_absolute': data.get('is_header_absolute', False)
        }
        page.with_context(no_cow=True).write(vals)
        return super(Page, self).save_page_info(website_id, data)

    def get_page_properties(self):
        return super(Page, self.with_context(read_is_header_absolute=True)).get_page_properties()

    def read(self, fields=None, load='_classic_read'):
        if self.env.context.get('read_is_header_absolute') and fields:
            fields.append('is_header_absolute')
        return super(Page, self).read(fields, load)
