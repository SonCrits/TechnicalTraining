from odoo import fields, models

class Survey(models.Model):
    _inherit = 'survey.survey'
    
    admission_id = fields.Many2one('education.admission', string='Admission')
