{
    'name': "Education Fees",
    'name_vi_VN': "Học phí",

    'summary': """
Config and compute fees
""",
    'summary_vi_VN': """
Cấu hình và quản lý học phí
""",

    'description': """
What it does
============
Config and compute fees

Key Features
============
* Config fees
* Setting fee discount
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô đun này làm gì
=================
Cấu hình và quản lý học phí.

Tính năng nổi bật
=================
* Cấu hình học phí
* Thiết lập ưu đãi học phí
    
Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Education',
    'version': '0.1.0',
    'depends': ['viin_education'],

    'data': [
        'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/menu_root.xml',
        'views/education_fee_term_views.xml',
        'views/education_student_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 299.9,
    'subscription_price': 8.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
