from odoo import fields, models


class FinalYearStudent(models.Model):
    _inherit = 'education.student'
    
    final_year = fields.Boolean(string='Final Year Student', related='class_group_id.final_year', store=True)
