from odoo import fields, models


class EductionClassGroup(models.Model):
    _inherit = 'education.class.group'
    
    final_year = fields.Boolean(string='Final Year Group')
