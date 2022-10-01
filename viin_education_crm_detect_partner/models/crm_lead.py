from odoo import models, api
from odoo.osv import expression


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    @api.model_create_multi
    def create(self, vals_list):
        records = super(CRMLead, self).create(vals_list)
        records.filtered(lambda r: not r.parent_id)._recognize_parent()
        return records

    def action_recognize_partner(self):
        super(CRMLead, self).action_recognize_partner()
        self._recognize_parent()

    def _recognize_parent(self):
        domain = self._get_recognize_parent_domain()
        partners = self.env['res.partner'].search(domain)
        parents = partners.filtered(lambda p: p.is_parent)
        for r in self:
            recognized_parents = r._match_parents(parents)
            if recognized_parents:
                r.parent_id = recognized_parents[0]

    def _get_parent_matching_criteria(self):
        """
        Return
        list: (lead_field, partner_field)
            List of tuples with lead field mapped with partner field
        """
        return [
            ('email_from', 'email'),
            ('phone', 'phone'),
            ('mobile', 'mobile')
        ]

    def _get_recognize_parent_domain(self):
        """
        Return
        list: domain
            Domain for matched parent criteria
        """
        domain = []
        criteria_fields = self._get_parent_matching_criteria()
        for lead_field, partner_field in criteria_fields:
            criteria = self.filtered(lambda r: getattr(r, lead_field)).mapped(lead_field)
            domain.append([(partner_field, 'in', criteria)])
        domain = expression.OR(domain)
        return domain

    def _match_parents(self, partners):
        self.ensure_one()
        match_parents = self.env['res.partner']
        criteria_fields = self._get_parent_matching_criteria()
        for lead_field, partner_field in criteria_fields:
            lead_field_val = getattr(self, lead_field)
            if lead_field_val:
                match_parents = partners.filtered(lambda p: getattr(p, partner_field) == lead_field_val)
                if match_parents:
                    break
        return match_parents

    def _match_partners(self, partners):
        detected_partners = super(CRMLead, self)._match_partners(partners)
        if detected_partners:
            if self.contact_name:
                detected_partners = detected_partners.filtered(lambda p: p.name == self.contact_name)
                if not detected_partners or len(detected_partners) == 1:
                    return detected_partners
                if self.customer_dob:
                    detected_partners = detected_partners.filtered(lambda p: p.dob == self.customer_dob)
            else:
                if self.customer_dob:
                    detected_partners = detected_partners.filtered(lambda p: p.dob == self.customer_dob)
                    if detected_partners:
                        return detected_partners
                student_detected_partners = detected_partners.filtered(lambda p: p.education_student_ids)
                if student_detected_partners:
                    return student_detected_partners

        return detected_partners
