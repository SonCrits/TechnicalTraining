from odoo import fields, models

class EducationAdmissionTag(models.Model):
    _name = 'education.admission.tag'
    _description = "Education Admission Tag"
    
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string='Color Index')
