from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    crm_default_source_id = fields.Many2one(
        'utm.source', string='Default Source', related='website_id.crm_default_source_id', readonly=False,
        help='Default Source for new leads created through the Contact Us form.')
