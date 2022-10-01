{
    'name': "Ethnicity",
    'name_vi_VN': "Dân tộc",

    'summary': """
    Ethnicities management
""",
    'summary_vi_VN': """
    Quản lý dân tộc""",

    'description': """
What it does
============
The module provides Ethnicities management features.

Key Features
============
* Ethnicities management
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Phân hệ cung cấp các tính năng về quản lý dân tộc.

Tính năng nổi bật
=================
* Quản lý dân tộc
    
Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Tools',
    'version': '0.1.0',
    'depends': ['base'],

    'data': [
        'data/res.partner.ethnicity.csv',
        'security/ir.model.access.csv',        
        'views/res_partner_ethnicity_views.xml',
        'views/res_partner_views.xml'
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
