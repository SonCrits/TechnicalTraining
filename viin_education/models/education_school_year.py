from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class EducationShoolYear(models.Model):
    _name = 'education.school.year'
    _description = 'School Year'
    
    name = fields.Char(string='Name', translate=True, required=True, readonly=False, compute='_compute_name', store=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today, required=True)
    end_date = fields.Date(string='End Date', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a School Year without deleting it.")
    
    _sql_constraints = [('class_name_unique', 'unique(name, company_id)', "The name of school year must be unique per company!")]
    
    @api.depends('start_date', 'end_date')
    def _compute_name(self):
        for r in self:
            if r.start_date and r.end_date:
                r.name = "%s - %s" % (r.start_date.year, r.end_date.year)
            else:
                r.name = False
    
    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        if self.filtered(lambda self: self.start_date and self.end_date and self.start_date > self.end_date):
            raise ValidationError(_("The School year start date must be earlier than or equal to end date."))
    
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(EducationShoolYear, self).copy(default=default)
