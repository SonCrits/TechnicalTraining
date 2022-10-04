from odoo import fields, models


class EducationStudentTuitionFeeWizard(models.TransientModel):
    _name = 'education.student.tuition.fee.wizard'
    _description = 'Education Student Tuition Fee Wizard'
    
    
    student_id = fields.Many2one('education.student', string='Student', required=True)
    student_state = fields.Selection(related='student_id.state', string='State')
    tuition_fee = fields.Float(string='Tuition Fee', required=True)
    math_point = fields.Float(string='Math Point')
    physical_point = fields.Float(string='Physical Point')
    chemistry_point = fields.Float(string='Chemistry Point')
    
    def action_confirm(self):
        self.student_id.tuition_fee = self.tuition_fee
        self.student_id.state = 'studying'
        self.student_id.math_point = self.math_point
        self.student_id.physical_point = self.physical_point
        self.student_id.chemistry_point = self.chemistry_point
