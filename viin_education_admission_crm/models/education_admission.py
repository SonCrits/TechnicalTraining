from odoo import models, fields, api

class EducationAdmission(models.Model):
    _inherit = 'education.admission'
    
    lead_ids = fields.One2many('crm.lead', 'admission_id', string='Leads', groups="sales_team.group_sale_salesman")
    leads_count = fields.Integer(string='Number Of Leads', compute='_compute_leads_count', groups="sales_team.group_sale_salesman")
    source_id = fields.Many2one('utm.source', string="Source", readonly=True, states={'draft': [('readonly', False)]},
                                help="Source to create leads or opportunities.")
    
    @api.depends('lead_ids')
    def _compute_leads_count(self):
        for r in self:
            r.leads_count = len(r.lead_ids)

    def action_view_lead(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('crm.crm_lead_opportunities')
        action['domain'] = [('admission_id', '=', self.id)]
        action['context'] = {'default_admission_id': self.id}
        return action
