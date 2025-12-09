# -*- coding: utf-8 -*-
{
    'name': "motsoft_partner_bank",

    'summary': "Mejora de las cuentas bancarias.",

    'description': """
Mejora las cuentas bancarias:
    * Descripción. Muy útil cuando el cliente tiene varias cuentas.
    """,

    'author': "David Sanromá",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_bank.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
