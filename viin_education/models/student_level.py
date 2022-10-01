from odoo import fields, models, _


class StudentLevel(models.Model):
    _name = 'student.level'
    _description = 'Student Level'
    _order = 'sequence'
    
    name = fields.Char(string='Name', translate=True, required=True)
    sequence = fields.Integer(string='Sequence', default=1, readonly=True)
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a student level without deleting it.")
    
    _sql_constraints = [('name_unique', 'unique(name)', "The name of the student level must be unique!")]

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(StudentLevel, self).copy(default=default)
