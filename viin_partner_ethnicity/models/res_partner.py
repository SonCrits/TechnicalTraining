from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    ethnicity_id = fields.Many2one('res.partner.ethnicity', string='Ethnicity', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    
    @api.onchange('ethnicity_id')
    def _onchange_ethnicity_id(self):
        if self.ethnicity_id:
            self.country_id = self.ethnicity_id.country_id
            
    @api.onchange('country_id')
    def _onchange_country_id(self):
        super(ResPartner, self)._onchange_country_id()
        if self.country_id and self.country_id != self.ethnicity_id.country_id:
            self.ethnicity_id = False
