from ast import literal_eval
from odoo import fields, models, api


class EducationStudent(models.Model):
    _inherit = 'education.student'
    
    opportunity_of_student_ids = fields.One2many('crm.lead', 'student_id', string='Opportunity of Student')
    opportunity_student_count = fields.Integer(string='Opportunity of Student Count', compute='_compute_opportunity_student_count', store=True)
    
    @api.depends('opportunity_of_student_ids')
    def _compute_opportunity_student_count(self):
        for r in self:
            r.opportunity_student_count = len(r.opportunity_of_student_ids)
    
    def action_view_opportunity_student(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('crm.crm_lead_action_pipeline')
        opportunity_of_student_ids = self.opportunity_of_student_ids
        opportunity_student_count = self.opportunity_student_count
        context = action['context']
        if not isinstance(action['context'], dict):
            context = literal_eval(action['context'])
        context.update({'default_partner_id': self.partner_id.id})
        action['context'] = context
        if opportunity_student_count == 1:
            form = self.env.ref('crm.crm_lead_view_form', False)
            action['views'] = [(form and form.id or False, 'form')]
            action['res_id'] = opportunity_of_student_ids.id
        else:
            action['domain'] = [('id', 'in', opportunity_of_student_ids.ids)]
        return action
