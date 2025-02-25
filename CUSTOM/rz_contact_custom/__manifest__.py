# -*- coding: utf-8 -*-
{
    'name': "rz_contact_custom",

   'summary': """
        Add default filter on modul Contact
        """,

    'description': """
            022025:
                *   Add default filter on modul Contact.\n
    """,

   'author': "UR Company",
    'website': "rizkidiansaputro@gmail.com",
    'images':"",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',


    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/contact_filter_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
