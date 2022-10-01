from ast import literal_eval
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    opportunity_of_parent_ids = fields.One2many('crm.lead', 'parent_id', string='Opportunity of Parent')
    opportunity_parent_count = fields.Integer(string='Opportunity of Parent counter', compute='_compute_opportunity_parent_count', store=True)
    
    @api.depends('opportunity_of_parent_ids')
    def _compute_opportunity_parent_count(self):
        for r in self:
            r.opportunity_parent_count = len(r.opportunity_of_parent_ids)
     
    def action_view_opportunity_parent(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('crm.crm_lead_action_pipeline')
        opportunity_of_parent_ids = self.opportunity_of_parent_ids
        opportunity_parent_count = self.opportunity_parent_count
        context = action['context']
        if not isinstance(action['context'], dict):
            context = literal_eval(action['context'])
        context.update({'default_parent_id': self.id})
        action['context'] = context
        if opportunity_parent_count == 1:
            form = self.env.ref('crm.crm_lead_view_form', False)
            action['views'] = [(form and form.id or False, 'form')]
            action['res_id'] = opportunity_of_parent_ids.id
        else:
            action['domain'] = [('id', 'in', opportunity_of_parent_ids.ids)]
        return action
