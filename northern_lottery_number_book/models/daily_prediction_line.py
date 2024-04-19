from odoo import fields, models, api, _


class DailyPredictionLine(models.Model):
    _name = 'daily.prediction.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Daily Prediction Line'

    name = fields.Char(string='Name', default=lambda self: _('New'))
    guess_nb = fields.Char(string='Guess Number', required=True)
    price_unit = fields.Float(string='Price Unit', required=True, help="Số tiền mà khách hàng này thực hiện Dự đoán")
    rate = fields.Float(string='Rate', compute='_compute_rate', help="Tỷ lệ phần thưởng mà đối tác này muốn dự đoán")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, required=True)
    winning_amount = fields.Float(string='Wining Amount', compute='_compute_winning_amount', store=True,
        help="Số tiền mà khách hàng này nhận được nếu dự đoán trúng")
    prediction_id = fields.Many2one('daily.prediction', string='DailyPrediction')
    partner = fields.Many2one('res.partner', string='Partner', required=True)
    lottery_rule = fields.Many2one('lottery.commission.rule', string='Lottery Rule', required=True)
    date = fields.Date(ralated='prediction_id.date')
    daily_result_ids = fields.Many2many(
        'daily.draw.result', 'prediction_line_id', 'daily_result_precdition_line_rel', 'daily_result_id',
        string='Daily Results', compute='_compute_daily_result_ids', store=True,
        help="Kết quả hàng ngày"
    )
    is_winner = fields.Boolean(string='Is Winner', compute='_compute_is_winner',
        help="Dòng dự đoán này có trúng hay không")
    commission = fields.Float(string='Commission', compute='_compute_commission', store=True)
    
    @api.depends('prediction_id.daily_result_ids')
    def _compute_daily_result_ids(self):
        for r in self:
            r.daily_result_ids = r.prediction_id.daily_result_ids
    
    @api.depends('daily_result_ids', 'guess_nb', 'lottery_rule')
    def _compute_is_winner(self):
        for r in self:
            list_result = []
            for result in r.daily_result_ids:
                nb_of_digits = r.lottery_rule.nb_of_digits
                list_result.append(str(result)[-nb_of_digits])
                special_result = str(r.daily_result_ids.filtered(lambda r: r.type == 'special')[:1].number)[-nb_of_digits]
            if r.guess_nb in list_result:
                if not r.lottery_rule.is_special:
                    r.is_winner = True
                else:
                    if r.guess_nb ==  special_result:
                        r.is_winner = True
            else:
                r.is_winner = False
    
    @api.depends('lottery_rule')
    def _compute_rate(self):
        for r in self:
            r.rate = r.lottery_rule.winning_rate_from_users
    
    @api.depends('rate', 'price_unit', 'is_winner')
    def _compute_winning_amount(self):
        for r in self:
            if r.is_winner:
                r.winning_amount = r.price_unit * r.rate
            else:
                r.winning_amount = 0.0
    
    @api.depends('winning_amount', 'lottery_rule')
    def _compute_commission(self):
        for r in self:
            r.commission = r.winning_amount * (r.lottery_rule.commission_rate + r.lottery_rule.margin_rate)
