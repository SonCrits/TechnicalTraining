from odoo import fields, models

class Survey(models.Model):
    _inherit = 'survey.survey'
    
    create_lead = fields.Boolean(string='Create Lead', help="Create a Lead after submit a Survey.")
    lead_ids = fields.One2many('crm.lead', 'survey_id', string='Leads')
    leads_count = fields.Integer(string='Number of Leads', compute='_compute_leads_count')

    def _compute_leads_count(self):
        for r in self:
            r.leads_count = len(r.lead_ids)

    def action_view_lead(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('crm.crm_lead_opportunities')
        action['domain'] = [('survey_id', '=', self.id)]
        return action
