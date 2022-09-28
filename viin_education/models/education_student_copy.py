from odoo import models, fields


class EducationStudentCopy(models.Model):
    _name = 'education.student.copy'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Education Student - Copy'
    
    parent_id = fields.Many2one('res.partner', string='Student', ondelete='restrict', required=True)
    DOB = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age')
