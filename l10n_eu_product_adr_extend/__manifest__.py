# -*- coding: utf-8 -*-
{
    'name': "l10n_eu_product_adr_extend",

    'summary': """
        Aggiunge full name string""",

    'description': """
        Aggiunge full name string
    """,

    'author': "Alpha Elettronica s.r.l.",
    'website': "https://www.alphaelettronica.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['l10n_eu_product_adr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_product.xml',
    ],
}