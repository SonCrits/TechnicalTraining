from odoo import models, fields

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    lead_ids = fields.One2many('crm.lead', 'user_input_id', string='Leads')
    
    def _prepare_lead_vals(self):
        self.ensure_one()
        vals = {
            'user_input_id': self.id,
            'type': 'lead',
            'user_id': False
            }
        for line in self.user_input_line_ids:
            if line. question_id.lead_field_id:
                val = False
                if line.answer_type == 'char_box':
                    val = line.value_char_box
                elif line.answer_type == 'numerical_box':
                    val = line.value_numerical_box
                elif line.answer_type == 'date':
                    val = line.value_date
                elif line.answer_type == 'datetime':
                    val = line.value_datetime
                elif line.answer_type == 'text_box':
                    val = line.value_text_box
                elif line.answer_type == 'suggestion':
                    val = line.suggested_answer_id.value
                
                vals.update({
                    line.question_id.lead_field_id.name: val
                    })
        if not vals.get('name', False):
            vals.update({
                'name': self.survey_id.title,
                })
        return vals

    def _prepare_lead_vals_list(self):
        vals_list = []
        for r in self:
            if not r.survey_id.create_lead:
                continue
            vals = r._prepare_lead_vals()
            vals_list.append(vals)
        return vals_list

    def _mark_done(self):
        res = super(SurveyUserInput, self)._mark_done()
        leads_vals_list = self._prepare_lead_vals_list()
        self.env['crm.lead'].create(leads_vals_list)
        return res
