{
    'name': "Education Final Year Student Management",
    'name_vi_VN': "Quản Lý Học Sinh Cuối Cấp",

    'summary': """
    Final year student management
""",
    'summary_vi_VN': """
    Quản học sinh cuối cấp.""",

    'description': """
What it does
============
Allows marking students as final-year students.

Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Cho phép đánh dấu học sinh là học sinh cuối cấp.

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
        'views/education_class_group_views.xml',
        'views/education_student_views.xml',
        ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
