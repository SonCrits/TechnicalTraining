from odoo import models, fields


class StudentLevel(models.Model):
    _name = 'student.level'
    _description = 'Student Level'
    _rec_name = 'code'
    _order = 'sequence, name'
    
    name = fields.Char(string="Name", translate=True, required=True)
    code = fields.Char(string="Code", required=True)
    sequence = fields.Integer(string="Sequence", default=1)
