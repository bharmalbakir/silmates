from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    purchase_line_id = fields.Many2one('purchase.order.line', string='Purchase Order Line')
