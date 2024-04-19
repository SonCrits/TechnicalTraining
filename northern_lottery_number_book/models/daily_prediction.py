from odoo import fields, models, api, _


class DailyPrediction(models.Model):
    _name = 'daily.prediction'
    _description = 'Daily Predictions'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', default=lambda self: _('New'))
    date = fields.Date(string='Date', default=fields.Date.context_today)
    line_ids = fields.One2many('daily.prediction.line', 'prediction_id', string='Daily Prediction Lines')
    daily_result_ids = fields.One2many('daily.draw.result', 'prediction_id', string='Daily Draw Result')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, required=True)
    commission = fields.Float(string='Commission Fees', compute='_compute_commission_fee', store=True)
    price_total = fields.Float(string='Price Total', compute='_compute_price_total', store=True)
    winning_price_total = fields.Float(string='Winning Price Total', compute='_compute_winning_price_total', store=True)
    
    @api.depends('line_ids.commission')
    def _compute_commission_fee(self):
        for r in self:
            r.commission = sum(r.line_ids.mapped('commission'))
    
    @api.depends('line_ids.price_unit')
    def _compute_price_total(self):
        for r in self:
            r.price_total = sum(r.line_ids.mapped('price_unit'))
    
    @api.depends('line_ids.winning_amount')
    def _compute_winning_price_total(self):
        for r in self:
            r.winning_price_total = sum(r.line_ids.mapped('winning_amount'))
