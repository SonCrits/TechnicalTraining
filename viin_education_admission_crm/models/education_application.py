from odoo import fields, models


class EducationApplication(models.Model):
    _inherit = 'education.application'

    lead_id = fields.Many2one('crm.lead', string="Lead", tracking=True, groups="sales_team.group_sale_salesman",
                              help="The lead that generate this application")
