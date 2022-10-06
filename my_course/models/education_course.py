from odoo import models, fields


class EducationCourse(models.Model):
    _name = 'education.course'
    _description = 'Education Course'
    
    name = fields.Char(string='Name', required=True, translate=True)
    price = fields.Float(string='Price')
    image = fields.Binary(string='Image')
    description = fields.Html(string='Description')
