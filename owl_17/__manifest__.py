# -*- coding: utf-8 -*-
{
    'name': "OWL 17",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    'assets': {
        'web.assets_backend': [
            # 'owl_17/static/src/components/listView/listView.css'
            'owl_17/static/src/components/listView/listView.js'
            'owl_17/static/src/components/listView/listView.xml'
        ]
    },
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
}
