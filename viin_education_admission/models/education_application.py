from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class EducationApplication(models.Model):
    _name = 'education.application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Education Application'
    
    name = fields.Char(string='Name', required=True, tracking=1)
    student_id = fields.Many2one('education.student', string='Student', tracking=1)
    admission_id = fields.Many2one('education.admission', string='Admission', tracking=1)
    application_date = fields.Date(string='Application Date', default=fields.Date.today, tracking=1)
    admission_date = fields.Date(string='Admission Date', default=fields.Date.today, tracking=1)
    state = fields.Selection(string='State', selection=[('draft', 'Draft'),
                                        ('confirmed', 'Confirmed'),
                                        ('cancelled', 'Cancelled')], default='draft', required=True , readonly=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a Application without deleting it.")
    
    _sql_constraints = [('student_admission_unique', 'unique(student_id, admission_id)', "The student - admission must be unique!")]
    
    @api.constrains('application_date', 'admission_date')
    def _check_date(self):
        if self.filtered(lambda self: self.application_date and self.admission_date and self.application_date > self.admission_date):
            raise ValidationError(_("The Application date must be earlier than or equal to the admission date."))
    
    @api.onchange('student_id')
    def _onchange_student_id(self):
        for r in self:
            if r.student_id:
                r.name = r.student_id.name
    
    def action_confirm(self):
        return self.write({'state': 'confirmed'})
         
    
    def action_cancel(self):
        for r in self:
            r.student_id.with_context(test_archive=True).test_archive_student()
        self.write({'state': 'cancelled'})
    
    def action_draft(self):
        return self.write({'state': 'draft'})
