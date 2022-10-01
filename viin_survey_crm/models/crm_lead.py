from odoo import models, fields

class Lead(models.Model):
    _inherit = "crm.lead"
    
    user_input_id = fields.Many2one('survey.user_input', string='Survey Result')
    survey_id = fields.Many2one('survey.survey', string='Survey', related='user_input_id.survey_id')
