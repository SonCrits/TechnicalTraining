{
    'name': "Admission Management",
    'name_vi_VN': "Quản lý Tuyển sinh",

    'summary': """
    Module admissions management
""",
    'summary_vi_VN': """
    Phân hệ quản lý chương trình tuyển sinh""",

    'description': """
What it does
============
The module provides Admissions management features.

Key Features
============
* Admissions management
* Applications management
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Phân hệ cung cấp các tính năng quản lý tuyển sinh.

Tính năng nổi bật
=================
* Quản lý chương trình tuyển sinh
* Quản lý đăng ký nhập học
    
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
        'views/education_admission_views.xml',
        'views/education_application_views.xml',
        'views/education_admission_tag_views.xml',
        ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 199.9,
    'subscription_price': 4.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
