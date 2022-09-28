from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import date


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Education Student'
    
    name = fields.Char(string="Student Name", required=True, translate=True)
    student_code = fields.Char(string="Student Code", required=True, index=True, help="Student Id is Unique")
    gender = fields.Selection(selection=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ], string="Gender", default="male")
    DOB = fields.Date(string="Date Of Birth")
    age = fields.Integer(
        string='Age', 
        compute="_compute_age", 
        inverse="_inverse_age", 
        search="_search_age",
        store=False,
        compute_sudo=True
    )
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string="Internal Notes")
    description = fields.Html(string="Description", sanitize=True, strip_style=False)
    attached = fields.Binary(string="Attached File", groups="base.group_user")
    total_score = fields.Float(string="Total Score")
    write_date = fields.Datetime(string="Last Updated On")
    currency_id = fields.Many2one('res.currency', string="Currency")
    amount_paid = fields.Monetary(string='Amount Paid')
    class_id = fields.Many2one('education.class', string="Class", ondelete='restrict')
    school_id = fields.Many2one('education.school', string="School")
    school_code = fields.Char(related='school_id.code', string='School Code')
    school_address = fields.Char(related='school_id.address', string="School Address")
    state = fields.Selection([
        ('new', 'New'),
        ('studying', 'Studying'),
        ('off', 'Off')
    ], string="Status", default="new")
    
    _sql_constraints = [
        ('student_code_unique', 'unique(student_code)', "The student code must be unique!"),
        ('check_total_score', 'CHECK(total_score >= 0)', "The total score must be greater than 0!")
    ]
    
    @api.constrains('DOB')
    def _check_date_of_birth(self):
        for reco in self:
            if reco.DOB > fields.Date.today():
                raise ValidationError(_("Date of birth must be in the past"))
    
    @api.depends('DOB')
    def _compute_age(self):
        year_now = fields.Date.today().year
        for reco in self:
            if reco.DOB:
                reco.age = year_now - reco.DOB.year
            else:
                reco.age = 0
                
    def _inverse_age(self):
        for r in self:
            if r.age and r.DOB:
                current_year = fields.Date.today().year
                dob_year = current_year - r.age
                dob_month = r.DOB.month
                dob_day = r.DOB.day
                DOB = date(dob_year, dob_month, dob_day)
                r.DOB = DOB
        
    def _search_age(self, opera, value):
        new_year = fields.Date.today().year - value
        new_value = date(1, 1, new_year)
        opera_map = {'>': '<', '>=': '<=', '<': '>', '<=': '>='}
        new_operator = opera_map.get(opera, opera)
        return [('DOB', new_operator, new_value)]
    
    @api.model
    def is_allowed_state(self, current_state, new_state):
        allowed_state = [(
            ('new', 'studying'),
            ('studying', 'off'),
            ('off', 'studying'),
            ('new', 'off')
        )]
        return (current_state, new_state) in allowed_state
    
    def check_student_state(self, state):
        for student in self:
            if student.is_allowed_state(student.state, state):
                student.state = state
            else:
                continue
            
    def change_to_new(self):
        self.check_student_state('new')
        
    def change_to_studying(self):
        self.check_student_state('studying')
        
    def change_to_off(self):
        self.check_student_state('off')
        
    def action_open_student_wizard_form(self):
        return {
            'viewmode': 'form'
        }
