from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_viin_education_admission = fields.Boolean(string='Admissions Management')
    module_viin_education_fees = fields.Boolean(string='Education Fees')
    module_viin_education_crm = fields.Boolean(string='CRM Integration')
    module_viin_education_admission_crm = fields.Boolean(string='Admissions CRM')
    module_viin_education_admission_survey_crm = fields.Boolean(string='Admissions Survey CRM')
    module_viin_education_crm_detect_partner = fields.Boolean(string='Education CRM detect Partner')
    module_viin_education_final_year = fields.Boolean(string='Education Final Year')
