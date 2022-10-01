from ast import literal_eval
from odoo import models, fields, api

class EducationAdmission(models.Model):
    _inherit = 'education.admission'
    
    survey_ids = fields.One2many('survey.survey', 'admission_id', string='Surveys')
    surveys_count = fields.Integer(string='Number Of Surveys', compute='_compute_surveys_count')
    
    @api.depends('survey_ids')
    def _compute_surveys_count(self):
        for r in self:
            r.surveys_count = len(r.survey_ids)

    def action_view_survey(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('survey.action_survey_form')
        action['domain'] = [('admission_id', '=', self.id)]
        context = action['context']
        if not isinstance(action['context'], dict):
            context = literal_eval(action['context'])
        context.update({'default_admission_id': self.id})
        action['context'] = context
        return action
