from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def action_purchase_history(self):
        self.ensure_one()
        product_id = self.order_line.mapped('product_id').id
        if not product_id:
            return

        # Fetch all purchase orders lines for the given product
        purchase_order_lines = self.env['purchase.order.line'].search([('product_id', '=', product_id)])
        purchase_orders = purchase_order_lines.mapped('order_id')

        # Return an action to display the purchase orders
        return {
            'name': 'Product History',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            'domain': [('id', 'in', purchase_orders.ids)],
            'context': dict(self._context),
        }
