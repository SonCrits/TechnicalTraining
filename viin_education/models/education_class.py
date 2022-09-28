from odoo import fields, models


class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Class'
    
    name = fields.Char(string="Class Name", translate=True, required=True)
    code = fields.Char(string="Code", copy=False)
    school_id = fields.Many2one('education.school', string="School", required=True)
    teacher_ids = fields.Many2many('res.partner', string="Teachers")
    student_ids = fields.One2many('education.student', 'class_id', string="Students")
    
    def get_all_students(self):
        student = self.env["education.student"]
        student_list = student.search([])
        print("All Student: ", student_list)
    
    def create_classes(self):
        student_1 = {
            'name': 'Nguyen Van A'
        }
        student_2 = {
            'name': 'Nguyen Van B'
        }
        create_value = {
            'name': 'New Class',
            'student_ids': [
                (0, 0, student_1),
                (0, 0, student_2)
            ]
        }
        return self.env['education.class'].create(create_value)
