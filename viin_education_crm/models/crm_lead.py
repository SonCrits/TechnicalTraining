from odoo import fields, models, api, _
from odoo.exceptions import UserError
from odoo.tools import email_split


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    parent_name = fields.Char(string='Parent Name')
    parent_id = fields.Many2one('res.partner', string='Parent')
    student_id = fields.Many2one('education.student', string='Student', compute='_compute_student_id', readonly=False, store=True)
    partner_id = fields.Many2one(compute='_compute_partner_id', readonly=False, store=True)

    @api.depends('student_id')
    def _compute_partner_id(self):
        for r in self:
            r.partner_id = r.student_id.partner_id

    @api.depends('partner_id')
    def _compute_student_id(self):
        for r in self:
            r.student_id = r.partner_id.education_student_ids[:1] if r.partner_id.education_student_ids else False

    def _create_student(self):
        self.ensure_one()
        """ Create a student from lead data
            :returns education.student record
        """
        if not self.contact_name:
            raise UserError(_("Can't create student because the contact name on lead %s is empty.") % self.name)
        val = self._prepare_education_student_data()
        return self.env['education.student'].create(val)
     
    def _prepare_education_student_data(self):
        self.ensure_one()
        return {
            'name': self.contact_name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'comment': self.description,
            'phone': self.phone,
            'mobile': self.mobile,
            'email': email_split(self.email_from)[0] if email_split(self.email_from) else False,
            'title': self.title.id,
            'function': self.function,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'type': 'contact',
            'dob': self.customer_dob
            }
        
    def _prepare_parent_values(self):
        self.ensure_one()
        return {
            'name': self.parent_name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'type': 'contact',
            'is_parent': True
            }
        
    def _create_lead_parent(self):
        self.ensure_one()
        """ Create a parent from lead data
            :returns res.partner record
        """
        if not self.parent_name:
            raise UserError(_("Can't create parent because the parent name on lead %s is empty.") % self.name)
        val = self._prepare_parent_values()
        return self.env['res.partner'].create(val)
    
    def _convert_opportunity_data(self, customer, team_id=False):
        upd_values = super(CrmLead, self)._convert_opportunity_data(customer, team_id)
        upd_values.update({
            'parent_id': self.parent_id.id
            })
        return upd_values
    
    def _add_student_parent_relationship(self, relationship):
        """
        Allow add relation between student and parent after convert leads to opportunities.
        """
        for r in self:
            if r.parent_id and r.student_id:
                exists_parents = r.student_id.parent_ids.filtered(lambda p: p.parent_id.id == r.parent_id.id)
                if not exists_parents:
                    self.env['student.relation'].create(self._prepare_student_relation_values(r.parent_id, r.student_id, relationship))
                    
    def _prepare_student_relation_values(self, parent, student, relationship):
        res = {
            'parent_id': parent.id,
            'student_id': student.id,
            'relationship_id': relationship.id
        }
        return res
