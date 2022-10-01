from odoo import fields, models


class EductionSchool(models.Model):
    _name = 'education.school'
    _description = 'School'
    
    name = fields.Char(string='Name', translate=True, required=True)
    code = fields.Char(string='Code', copy=False)
    company_id = fields.Many2one('res.company', string='Company')
    active = fields.Boolean(default=True,
            help="By unchecking the active field, you may hide a school without deleting it.")
