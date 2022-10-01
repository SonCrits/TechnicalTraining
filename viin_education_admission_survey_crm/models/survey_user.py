from odoo import models

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'
    
    def _prepare_lead_vals(self):
        self.ensure_one()
        res = super(SurveyUserInput, self)._prepare_lead_vals()
        res.update({
            'admission_id': self.survey_id.admission_id.id if self.survey_id.admission_id else False,
            'company_id': self.survey_id.admission_id.company_id.id if self.survey_id.admission_id.company_id else False
            })
        return res
