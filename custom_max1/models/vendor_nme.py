from odoo import models, fields


class VendorName(models.Model):
    _inherit = 'res.partner'

    contact = fields.Char(string="Contact Name")
