# -*- coding: utf-8 -*-
{
    'name': "rz_is_customer_vendor",

    'summary': """
        Add Field Is a Customer and Is a Vendor on Contact
        """,

    'description': """
            022025:
                *   Add Field Is a Customer And Is a Vendor checkbox Into The Partner Form For Identification.\n
                *   Easy To Use.\n
                *   User Can Manually Set / Unset Customer and Vendor Checkbox.\n
                *   Add Customer Filter In Sale Order.\n
                *   Add Vendor Filter In Purchase Order.
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
    'depends': ['base','account','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
