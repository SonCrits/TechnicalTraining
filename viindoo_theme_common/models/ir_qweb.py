from odoo import models


# Use lazy-loading on iframe to speed up web page loading
# TODO: remove this if it's added to Odoo
class Qweb(models.AbstractModel):
    _inherit = 'ir.qweb'

    def _post_processing_att(self, tagName, atts, options):
        atts = super()._post_processing_att(tagName, atts, options)
        if tagName == 'iframe' and 'loading' not in atts:
            atts['loading'] = 'lazy'
        return atts
