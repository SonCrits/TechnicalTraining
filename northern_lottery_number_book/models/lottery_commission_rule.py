from odoo import models, fields, api


class LotteryCommissionRule(models.Model):
    _name = 'lottery.commission.rule'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Lottery Commission Rule'

    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    nb_of_digits = fields.Integer(string='Number Of Digits', required=True, tracking=True,
        help="The number of digits that this rule applies to\n"
        "For example, for the game 'lô' it is 2, for 'đề' it is 2, and for 'ba càng' it is 3...")
    winning_rate_from_vendor = fields.Float(string='Wining Percentage From Vendor', required=True,
        help="Percentage of the prize money that the winning predictor will receive from the provider based on their bet amount.")
    winning_rate_from_users = fields.Float(string='Wining Percentage From Users', required=True,
        help="Percentage of the prize money that the winning predictor will receive from the company (or the person organizing the lottery) based on their bet amount.")
    margin_rate = fields.Float(string='Margin Rate.',
        compute='_compute_margin_rate', store=True, tracking=True,
        help="Margin rate earned by the person recording the bet")
    commission_rate = fields.Float(string='Commission Rate', help="Tỷ lệ mà Nhà cung cấp chia lại cho nhân viên ghi đề")
    is_special = fields.Boolean(string='Compare with special prize only',
        help="Xác định quy tắc lottery này chỉ so sánh với giải đặc biệt trong ngày")

    @api.depends('winning_rate_from_vendor', 'winning_rate_from_users')
    def _compute_margin_rate(self):
        for r in self:
            r.margin_rate = r.winning_percentage_from_users - r.winning_percentage_from_vendor
