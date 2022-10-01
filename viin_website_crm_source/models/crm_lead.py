from odoo import models


class Lead(models.Model):
    _inherit = 'crm.lead'

    def website_form_input_filter(self, request, values):
        res = super(Lead, self).website_form_input_filter(request, values)
        res['source_id'] = values.get('source_id') or \
                            request.website.crm_default_source_id.id
        return res
