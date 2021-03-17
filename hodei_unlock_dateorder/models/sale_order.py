# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_order = fields.Datetime(readonly=False)

    def action_confirm(self):
        if self.date_order:
            date_order_saved = self.date_order
        super(SaleOrder, self).action_confirm()
        self.write({'date_order': date_order_saved})
        return True
