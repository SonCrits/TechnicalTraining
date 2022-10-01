from odoo import models


class EducationStudent(models.Model):
    _inherit = 'education.student'
    
    def test_archive_student(self):
        self.ensure_one()
        if self.env.context.get('test_archive', False):
            self.active = False
