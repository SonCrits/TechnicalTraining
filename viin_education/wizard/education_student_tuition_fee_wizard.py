from odoo import fields, models


class EducationStudentTuitionFeeWizard(models.TransientModel):
    _name = 'education.student.tuition.fee.wizard'
    _description = 'Education Student Tuition Fee Wizard'
    
    
    student_id = fields.Many2one('education.student', string='Student', required=True)
    math_point = fields.Float(string='Math Point')
    physical_point = fields.Float(string='Physical Point')
    chemistry_point = fields.Float(string='Chemistry Point')
    
    def action_confirm(self):
        student_state = self.env.context.get('default_state')
        if student_state == 'new':
            self.student_id.tuition_fee = 4000000
        elif student_state == 'studying':
            self.student_id.tuition_fee = 2000000
        else:
            self.student_id.tuition_fee = 0
        self.math_point = self.student_id.math_point
        self.physical_point = self.student_id.physical_point
        self.chemistry_point = self.student_id.chemistry_point
