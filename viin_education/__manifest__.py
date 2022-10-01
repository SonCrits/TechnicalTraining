{
    'name': "Education Management",
    'name_vi_VN': "Quản lý giáo dục",

    'summary': """
    Module education management
""",
    'summary_vi_VN': """
    Phân hệ quản lý về lĩnh vực giáo dục.""",

    'description': """
What it does
============
The module provides management education features.

Key Features
============
* Students management
* Parents managemnt
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Phân hệ cung cấp các tính năng về quản lý giáo dục.

Tính năng nổi bật
=================
* Quản lý học sinh
* Quản lý liên hệ phụ huynh
    
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
    'depends': ['viin_partner_gender', 'to_partner_dob', 'to_partner_nationality', 'viin_partner_ethnicity', 'viin_base_district', 'mail'],

    'data': [
        'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/menu_root.xml',
        'views/res_config_settings_views.xml',
        'views/education_class_views.xml',
        'views/education_class_group_views.xml',
        'views/education_school_views.xml',
        'views/education_school_year_views.xml',
        'views/student_level_views.xml',
        'views/education_student_views.xml',
        'views/education_relationship_views.xml',
        'views/res_partner_views.xml'
        ],
    'demo': [
        'demo/education_school_demo.xml',
        'demo/education_class_group_demo.xml',
        'demo/education_class_demo.xml',
        'demo/student_level_demo.xml',
        'demo/education_relationship_demo.xml',
        'demo/education_school_year_demo.xml',
        'demo/education_student_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 199.9,
    'subscription_price': 4.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
