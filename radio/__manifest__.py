# -*- coding: utf-8 -*-
{
    'name': "radio",

    'summary': """
        Odoo module for learning coding Odoo modules""",

    'description': """
        Odoo module for learning coding Odoo modules
    """,

    'author': "Antonio Company",
    'website': "http://www.antoniocompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'demo/demo.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hr.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installabe': True,
    'application': True,

}
