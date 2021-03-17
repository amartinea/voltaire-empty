# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hodei Unlock OrderDate',
    'version': '1.1',
    'category': 'Sales/Sales',
    'summary': 'Hodei Unlock Order Date on Sale Order',
    'author': 'Arthur MARTINEAU <a.martineau@hodei.net>',
    'description': """
This module allow to modifiy order date on sale order at anytime.
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False
}
