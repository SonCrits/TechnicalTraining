from odoo import fields, models

class EducationFeeTerm(models.Model):
    _name = 'education.fee.term'
    _description = "Education Fees Terms"
    
    name = fields.Char(string='Fee Term', translate=True, required=True)
    discount = fields.Float(string='Discount (%)', required=True)
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    active = fields.Boolean('Active', default=True)
