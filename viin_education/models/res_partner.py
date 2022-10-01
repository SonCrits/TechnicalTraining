from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_parent = fields.Boolean(string='Is Parent')
    student_ids = fields.One2many('student.relation', 'parent_id', string='Student Relation', groups='viin_education.viin_education_group_user')
    education_student_ids = fields.One2many('education.student', 'partner_id', string='Students', groups='viin_education.viin_education_group_user')
    studying_student_count = fields.Integer(string='Studying Student Count', compute='_compute_studying_student_count', store=True)
    is_teacher = fields.Boolean(string='Is Teacher')
    
    @api.depends('student_ids', 'student_ids.student_id.state')
    def _compute_studying_student_count(self):
        for r in self:
            studying_student_count = 0
            if r.student_ids:
                students = r.student_ids.filtered(lambda s: s.student_id.state == 'studying')
                studying_student_count = len(students)
            r.studying_student_count = studying_student_count
