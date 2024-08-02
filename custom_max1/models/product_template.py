from odoo import models, fields ,api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    resistance = fields.Char(string="Resistance")
    power_rating = fields.Char(string="Power Rating")
    package = fields.Char(string="Package")
    sub_category = fields.Many2one('product.product' , string="Sub Category")
    temp_coefficient = fields.Char(string="Temperature Coefficient")
    min_oper_temp = fields.Char(string="Minimum Operating Temperature")
    max_oper_temp = fields.Char(string="Maximum Operating Temperature")
    voltage_rating = fields.Char(string="Voltage Rating")
    remark = fields.Text(string="Remark")
    part_number = fields.Char(string="Part Number")
    manufacturer = fields.Char(string="Manufacturer")
    supplier = fields.Char(string="Supplier")
    value = fields.Char(string="Value")

    tolerance = fields.Char(string="Tolerance")
    watts = fields.Char(string="Watts")
    sub_qty = fields.Char(string=" Quantity")
    issued_qty = fields.Char(string="Issued Quantity")
    total_qty = fields.Char(string="Total Quantity")
    hsn_code = fields.Char(string="HSN Code")
    location = fields.Char(string="Location")
    hsn_desc = fields.Char(string="HSN Description")
    forward_voltage = fields.Char(string="Forward voltage")
    breakdown_voltage = fields.Char(string="Breakdown voltage")
    rev_voltage = fields.Char(string="Rev. Voltage")
    forward_current = fields.Char(string="Forward current")

    current_rating = fields.Char(string="Current rating")
    # power_dissipation = fields.Char(string="Power Dissipation")
    output_current = fields.Char(string="Output current")
    output_voltage = fields.Char(string="Output voltage")
    vol_type = fields.Char(string="Voltage Type")
    min_vlt = fields.Char(string="Minimun voltage")
    max_vlt = fields.Char(string="Maximum Voltage")
    load_capaci = fields.Char(string="Load capacitance")
    no_of_position = fields.Char(string="No.of position")
    pitch = fields.Char(string="Pitch")
    dsv = fields.Char(string="Drain to Source Voltage (Vdss)")
    vgs = fields.Char(string="VGS (max)")
    cc_m = fields.Char(string="Current - Collector (Ic) (Max)")

    new_quantity = fields.Integer(string="New Quantity", compute='_compute_new_quantity', store=True)

    @api.depends('sub_qty')
    def _compute_new_quantity(self):
        for product in self:
            # Your computation logic here to update new_quantity based on sub_qty
            product.new_quantity = product.sub_qty