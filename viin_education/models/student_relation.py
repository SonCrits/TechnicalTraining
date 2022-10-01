from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StudentRelation(models.Model):
    _name = 'student.relation'
    _description = 'Student Relation'
    
    parent_id = fields.Many2one('res.partner', string='Parent', required=True, ondelete='cascade', domain=[('is_parent', '=', True)])
    student_id = fields.Many2one('education.student', string='Student', required=True, ondelete='cascade')
    relationship_id = fields.Many2one('education.relationship', string='Relationship',required=True)
    is_contact_person = fields.Boolean(string='Is Contact Person')
    
    _sql_constraints = [('parent_student_unique','unique(parent_id, student_id)', "The parent and student must be unique per relationship!")]
