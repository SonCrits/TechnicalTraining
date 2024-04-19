from odoo import fields, models


class DailyDrawResult(models.Model):
    _name = 'daily.draw.result'
    _description = 'Daily Draw Result'

    name = fields.Char(string='Name', required=True, default='New')
    number = fields.Integer(string='Number', required=True)
    date = fields.Date(string='Date')
    type = fields.Selection(selection=[
        ('normal', 'Normal'),
        ('special', 'Special')
    ], string='Type', default='normal',
    help="Xác định bản ghi này có phải giải đặc biệt hay không")
    prediction_id = fields.Many2one('daily.prediction', string='Daily Precdiction')
