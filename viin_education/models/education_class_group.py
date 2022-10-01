from odoo import fields, models, _


class EductionClassGroup(models.Model):
    _name = 'education.class.group'
    _description = 'Education Class Group'
    _order = 'sequence'
    
    name = fields.Char(string='Name', translate=True, required=True)
    sequence = fields.Integer(string='Sequence', default=1, readonly=True)
    class_ids = fields.One2many('education.class', 'class_group_id', string='Class of Groups')
    company_id = fields.Many2one('res.company', string='Company')
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a Class Group without deleting it.")
    description = fields.Text(string='Description')
    
    _sql_constraints = [('name_unique', 'unique(name, company_id)', "The group name must be unique per company!")]
    
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(EductionClassGroup, self).copy(default=default)
