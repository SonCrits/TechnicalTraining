from ast import literal_eval
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import html_translate


class EducationAdmission(models.Model):
    _name = 'education.admission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Education Admission'
    
    name = fields.Char(string='Name', translate=True, required=True, tracking=1, readonly=True, states={'draft': [('readonly', False)]})
    school_year_id = fields.Many2one('education.school.year', string='School Year',  tracking=1, readonly=True, states={'draft': [('readonly', False)]})
    user_id = fields.Many2one('res.users', string='Responsible', tracking=1, default=lambda self: self.env.user,
        readonly=False, states={'done': [('readonly', True)], 'cancelled': [('readonly', True)]})
    start_date = fields.Date(string='Start Date', default=fields.Date.today, tracking=1, readonly=True, states={'draft': [('readonly', False)]})
    end_date = fields.Date(string='End date', default=fields.Date.today, tracking=1,
        readonly=False, states={'done': [('readonly', True)], 'cancelled': [('readonly', True)]})
    description = fields.Html(string='Description', translate=html_translate)
    color = fields.Integer("Color Index")
    state = fields.Selection(string='State', selection=[
        ('draft', 'New'),
        ('confirmed', 'Confirmed'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')], default='draft', required=True, readonly=True)
    application_ids = fields.One2many('education.application', 'admission_id', string='Application')
    application_count = fields.Integer(string='Application Count', compute='_compute_application_count', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean(default=True,
        help="By unchecking the active field, you may hide a Admission without deleting it.")
    tag_ids = fields.Many2many('education.admission.tag', string='Tags')
    expected_applications = fields.Integer(string='Expected Applications', readonly=True, states={'draft': [('readonly', False)]})
    new_application_count = fields.Integer(string='New Application', compute='_compute_new_application_count', store=True,
        help="Number of applications that are new in the flow (typically at first step of the flow)")
    confirm_application_count = fields.Integer(string='Confirmed Application', compute='_compute_confirm_application_count', store=True,
        help="Number of applications that are confirmed in the flow (typically at first step of the flow)")
    
    _sql_constraints = [('check_expected_applications', 'CHECK(expected_applications > 0)', 'The expected applications must be than zero' )]
    
    @api.depends('application_ids')
    def _compute_application_count(self):
        for r in self:
            r.application_count  = len(r.application_ids)
    
    @api.depends('application_ids.state')        
    def _compute_new_application_count(self):
        for r in self:
            r.new_application_count = self.env['education.application'].search_count(
                [('admission_id', '=', r.id), ('state', '=', 'draft')]
            )
    
    @api.depends('application_ids.state')
    def _compute_confirm_application_count(self):
        for r in self:
            r.confirm_application_count = self.env['education.application'].search_count(
                [('admission_id', '=', r.id), ('state', '=', 'confirmed')]
            )
    
    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        if self.filtered(lambda self: self.start_date and self.end_date and self.start_date > self.end_date):
            raise ValidationError(_("The Admission start date must be earlier than or equal to the end date."))
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
        
    def action_inprogress(self):
        self.write({'state': 'inprogress'})
        
    def action_done(self):
        self.write({'state': 'done'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})
    
    def action_draft(self):
        self.write({'state': 'draft'})
        
    def action_view_application(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('viin_education_admission.education_application_action')
        applications = self.application_ids
        application_count = self.application_count
        context = action['context']
        if not isinstance(action['context'], dict):
            context = literal_eval(action['context'])
        context.update({'default_admission_id': self.id})
        action['context'] = context
        if application_count == 1:
            form = self.env.ref('viin_education_admission.education_application_view_form')
            action['views'] = [(form and form.id or False, 'form')]
            action['res_id'] = applications.id
        else:
            action['domain'] = [('id', 'in', applications.ids)]
        return action
