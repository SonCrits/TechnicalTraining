from odoo import fields, models, _


class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'
    
    name = fields.Char(string='Name', required=True)
    class_group_id = fields.Many2one('education.class.group', string='Class Group', ondelete='restrict')
    next_class_id = fields.Many2one('education.class', string='Next Class')
    school_id = fields.Many2one('education.school', string='School', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a Class without deleting it.")
    
    _sql_constraints = [('class_name_unique', 'unique(name, company_id)', "The class name must be unique for each company!")]

    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(EducationClass, self).copy(default=default)
