from ast import literal_eval
from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    admission_id = fields.Many2one('education.admission', string='Admission', groups="viin_education_admission.viin_admission_group_user")
    source_id = fields.Many2one('utm.source', compute='_compute_source_id', store=True, readonly=False)
    application_ids = fields.One2many('education.application', 'lead_id', string='Applications',
                                      groups="viin_education_admission.viin_admission_group_user")
    application_count = fields.Integer(string='Number Of Applications', compute='_compute_application_count',
                                       groups="viin_education_admission.viin_admission_group_user")
    
    @api.depends('application_ids')
    def _compute_application_count(self):
        for r in self:
            r.application_count = len(r.application_ids)
    
    @api.depends('admission_id', 'admission_id.source_id')
    def _compute_source_id(self):
        for r in self:
            if r.admission_id and r.admission_id.source_id:
                r.source_id = r.admission_id.source_id.id
            else:
                r.source_id = False

    def _prepare_application_data(self):
        self.ensure_one()
        return {
            'name': self.student_id.name,
            'company_id': self.company_id.id,
            'student_id': self.student_id.id,
            'admission_id': self.admission_id.id,
            'admission_date': False,
            'lead_id': self.id
            }

    def _prepare_application_vals_list(self):
        vals_list = []
        for r in self:
            if r.student_id and r.admission_id:
                vals_list.append(r._prepare_application_data())
        return vals_list

    def convert_opportunity(self, partner_id, user_ids=False, team_id=False):
        res = super(CrmLead, self).convert_opportunity(partner_id, user_ids, team_id)
        application_val_list = self._prepare_application_vals_list()
        self.env['education.application'].create(application_val_list)
        return res

    def action_view_application(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('viin_education_admission.education_application_action')
        applications = self.application_ids
        application_count = self.application_count
        context = action['context']
        if not isinstance(action['context'], dict):
            context = literal_eval(action['context'])
        context.update({'default_lead_id': self.id})
        action['context'] = context
        if application_count == 1:
            form = self.env.ref('viin_education_admission.education_application_view_form')
            action['views'] = [(form and form.id or False, 'form')]
            action['res_id'] = applications.id
        else:
            action['domain'] = [('id', 'in', applications.ids)]
        return action
