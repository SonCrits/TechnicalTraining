{
    'name': "Education - CRM",
    'name_vi_VN': "Giáo dục - Tiềm năng/cơ hội",

    'summary': """
    The module connects CRM with an Education
""",
    'summary_vi_VN': """
    Phân hệ kết nối Tiềm năng/Cơ hội với Giáo dục""",

    'description': """
What it does
============
The module allows connect CRM with an Education application.

Key Features
============
* Create a new Student when convert leads to opportunity.
* Create a new Parent when convert leads to opportunity.
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Phân hệ cho phép kết nối giữa ứng dụng quản lý tiềm năng/cơ hội với giáo dục.

Tính năng nổi bật
=================
* Tạo Học sinh khi chuyển hóa tiềm năng thành cơ hội
* Tạo Phụ huynh khi chuyển hóa tiềm năng thành cơ hội
    
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
    'depends': ['viin_education', 'viin_crm_dob'],

    'data': [
        'wizards/crm_lead2opportunity_partner_views.xml',
        'wizards/crm_lead2opportunity_partner_mass_views.xml',
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
        'views/education_student_views.xml'
        ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'subscription_price': 1.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
