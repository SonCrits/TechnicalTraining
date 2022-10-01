from odoo import fields, models


class StudentSchoolStage(models.Model):
    _name = 'student.school.stage'
    _description = 'Student School Stage'
    _order = 'start_date desc'
    
    student_id = fields.Many2one('education.student', string='Student', ondelete='cascade', required=True)
    school_year_id = fields.Many2one('education.school.year', string='School year', required=True)
    start_date = fields.Date(string='Start Date', related='school_year_id.start_date', store=True)
    end_date = fields.Date(string='End Date', related='school_year_id.end_date', store=True)
    state = fields.Selection(string='State', selection=[('new', 'New'),
                                                        ('studying', 'Studying'),
                                                        ('finished', 'Finished'),
                                                        ('off', 'Off')
                                                        ], default='new', required=True)
    class_id = fields.Many2one('education.class', string='Class', required=True)
    
    _sql_constraints = [(
        'year_class_student_unique', 'unique(school_year_id, class_id, student_id)', "The student's class in a school year must be unique!"
        )]
