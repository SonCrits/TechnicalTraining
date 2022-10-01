from odoo import fields, models


class ResPartnerEthnicity(models.Model):
    _name = 'res.partner.ethnicity'
    _description = 'Ethnicity'
    
    name = fields.Char(string='Name', translate=True, required=True)
    code = fields.Char(string='Code', copy=False)
    country_id = fields.Many2one('res.country', string='Country')

    _sql_constraints = [
        ('code_unique', 'unique (code, country_id)', "The code of Ethnicity must be unique per country!")
    ]
