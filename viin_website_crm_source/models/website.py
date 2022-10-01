from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    crm_default_source_id = fields.Many2one(
        'utm.source', string='Default Source',
        help='Default Source for new leads created through the Contact Us form.')
