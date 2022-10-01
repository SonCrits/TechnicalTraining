from odoo import fields, models, _


class EducationRelationship(models.Model):
    _name = 'education.relationship'
    _description = 'Relationship'
    
    name = fields.Char(string='Name', translate=True, required=True)
    relation_type = fields.Selection(string='Relation Type', selection=[('father', 'Father'),
                                                                        ('mother', 'Mother'),
                                                                        ('other', 'Other')
                                                                        ], default='other', required=True)
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a Relationship without deleting it.")
    
    _sql_constraints = [('name_unique', 'unique(name)', "The name must be unique!")]

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(EducationRelationship, self).copy(default=default)
