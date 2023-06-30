# -*- coding: utf-8 -*-
{
    'name': "Quản Lý Tài Sản",
    'version': "1",
    'summary': """Assets management model""",
    'description': """Assets management information""",
    'author': "anhlh",
    'sequence': 1,
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/dts_assets_security.xml',
        'security/ir.model.access.csv',
        'views/dts_assets_view.xml',
        'views/dts_assets_table_view.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
