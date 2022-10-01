{
    'name': "Contact - Ethnicity",
    'name_vi_VN': "Liên hệ - Dân tộc",

    'summary': """
Bridge module between contact and ethnicity
""",
    'summary_vi_VN': """
Mô đun cầu nối giữa Liên hệ và Dân tộc
""",

    'description': """
What it does
============
Show ethnicity management menu.

Key Features
============
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô đun này làm gì
=================
Hiện thị menu để quản lý danh sách dân tộc.

Tính năng nổi bật
=================
    
Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Hidden',
    'version': '0.1.0',
    'depends': ['viin_partner_ethnicity','contacts'],

    'data': [
        'views/contact_views.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
