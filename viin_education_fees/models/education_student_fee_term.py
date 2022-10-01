from odoo import fields, models, api

class EducationStudentFeeTerm(models.Model):
    _name = 'education.student.fee.term'
    _description = "Education Student Fee Terms"
    
    student_id = fields.Many2one('education.student', string='Student', ondelete='cascade')
    fee_term_id = fields.Many2one('education.fee.term', string='Fee Term', required=True)
    discount = fields.Float(string='Discount (%)', required=True)
    description = fields.Text(string='Description')
    
    @api.onchange('fee_term_id')
    def _onchange_fee_term(self):
        if self.fee_term_id:
            self.discount = self.fee_term_id.discount
            self.description = self.fee_term_id.description
