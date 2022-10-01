from odoo import fields, models

class EducationStudent(models.Model):
    _inherit = 'education.student'
    
    fee_term_ids = fields.One2many('education.student.fee.term', 'student_id', string='Fees Terms', groups="viin_education_fees.group_education_fee_user")
