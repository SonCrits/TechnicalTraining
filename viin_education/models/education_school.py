from odoo import fields, models


class EducationSchool(models.Model):
    _name = 'education.school'
    _description = 'School'
    
    name = fields.Char(string="School Name", required=True, translate=True)
    code = fields.Char(string="Code", copy=False)
    class_ids = fields.One2many('education.class', 'school_id', string="Classes")
    address = fields.Char(string='Address')
