# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        This Library module is for odoo technical training
    """,

    'author': "__s_a_r_v_a_n_a___",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'views/library.xml',
    'views/category.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
