from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class EducationStudent(models.Model):
    _name = 'education.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Education Student'
    
    student_code = fields.Char(string='Student Code', copy=False)
    partner_id = fields.Many2one('res.partner', string='Student', ondelete="restrict", required=True)
    class_id = fields.Many2one('education.class', string='Class', ondelete="restrict", domain="[('class_group_id', '=?', class_group_id)]")
    class_group_id = fields.Many2one('education.class.group', string='Class Group', ondelete='restrict')
    school_id = fields.Many2one('education.school', related='class_id.school_id', string='School', store=True)
    school_stage_ids = fields.One2many('student.school.stage', 'student_id', string='Stage')
    state = fields.Selection(string='Status', selection=[('new', 'New'),
                                                         ('studying', 'Studying'),
                                                         ('off', 'Off')
                                                         ], default='new')
    student_level_id = fields.Many2one('student.level', string='Level', ondelete='restrict')
    parent_ids = fields.One2many('student.relation', 'student_id', string='Parents')
    attachment_ids = fields.Many2many('ir.attachment', 'education_student_ir_attachment_rel', 'attachment_id', 'student_id', string='Attachments')
    responsible_id = fields.Many2one('res.users', string='Responsible', tracking=True, help="Responsible for this student.")
    dropout_reason = fields.Text(string='Dropout Reason')
    tuition_fee = fields.Float(string='Tuition Free')
    math_point = fields.Float(string='Math Point')
    physical_point = fields.Float(string='Physical Point')
    chemistry_point = fields.Float(string='Chemistry Point')
    average_point = fields.Float(string='Average Point', compute='_compute_average_point')
    ref_ir_act_window = fields.Many2one('ir.actions.act_window', 'Sidebar action', readonly=True, copy=False,
                                        help="Sidebar action to make this template available on records "
                                             "of the related document model")
    
    _sql_constraints = [('student_code_unique', 'unique(student_code)', "The student code must be unique!")]

    @api.constrains('district_id', 'state_id')
    def _check_state(self):
        for r in self:
            if r.state_id and r.district_id and r.district_id.state_id != r.state_id:
                raise ValidationError(_("The district '%s' does not belong to state '%s'. Please select another!")\
                                      % (r.district_id.name, r.state_id.name))
                
    @api.constrains('district_id', 'country_id')
    def _check_country(self):
        for r in self:
            if r.country_id and r.district_id and r.district_id.country_id != r.country_id:
                raise ValidationError(_("The district '%s' does not belong to country '%s'. Please select another!")\
                                      % (r.district_id.name, r.country_id.name))
                
    @api.depends('math_point', 'physical_point', 'chemistry_point')
    def _compute_average_point(self):
        for r in self:
            if r.math_point == False and r.physical_point == False and r.chemistry_point == False:
                r.average_point = 0
            else:
                r.average_point = (r.math_point + r.physical_point + r.chemistry_point) / 3
    
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id and self.country_id != self.state_id.country_id:
            self.state_id = False
            self.district_id = False
        if self.country_id and self.country_id != self.ethnicity_id.country_id:
            self.ethnicity_id = False

    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id.country_id:
            self.country_id = self.state_id.country_id
        if self.state_id and self.state_id != self.district_id.state_id:
            self.district_id = False
        
    @api.onchange('district_id')
    def _onchange_district(self):
        if self.district_id:
            self.country_id = self.district_id.country_id
            self.state_id = self.district_id.state_id
            
    @api.onchange('ethnicity_id')
    def _onchange_ethnicity_id(self):
        if self.ethnicity_id:
            self.country_id = self.ethnicity_id.country_id
            
    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            self.class_group_id = self.class_id.class_group_id
            
    @api.onchange('class_group_id')
    def _onchange_class_group_id(self):
        if self.class_group_id and self.class_group_id != self.class_id.class_group_id:
            self.class_id = False
            
    def action_dropout(self):
        return self.env.ref('viin_education.education_student_dropout_wizard_action').read()[0]
    
    def action_tuition_fee(self):
        self.ensure_one()
        view = self.env.ref('viin_education.education_student_tuition_fee_view_wizard_form')
        return {
            'name': _("Chose Student"),
            'type': 'ir.actions.act_window',
            'res_model': 'education.student.tuition.fee.wizard',
            'views': [(view.id, 'form')],
            'target': 'new',
            'context': {
                'default_student_id': self.id,
                'state': self.state
            }
        }
