# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_order = fields.Datetime(readonly=False)

    def action_confirm(self):
        for order in self:
            if order.date_order:
                date_order_saved = order.date_order
            super(order).action_confirm()
            order.write({'date_order': date_order_saved})
        return True
