from odoo import fields, models


class EducationCourse(models.Model):
    _name = 'education.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", required=True, translate=True)
    image = fields.Binary(string="Image Course")
    description = fields.Html(string="Description")
