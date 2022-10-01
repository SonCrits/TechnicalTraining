{
    'name': "Admission - CRM",
    'name_vi_VN': "Tuyển sinh - CRM",

    'summary': """
    Admission and CRM Integration
""",
    'summary_vi_VN': """
    Tích hợp Tuyển sinh và CRM""",

    'description': """
What it does
============
The module connects Admission Management and Education - CRM modules.

Key Features
============
* Link Admission to Lead/Opportunity.
* Automatically generate Application when convert Lead to Opportunity.
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Mô đun này kết nối mô đun Quản lý Tuyển sinh và mô đun Giáo dục - CRM.

Tính năng nổi bật
=================
* Liên kết chương trình tuyển sinh tới Tiềm năng/Cơ hội.
* Tự động tạo Đăng ký nhập học khi chuyển Tiềm năng thành Cơ hội.
    
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
    'depends': ['viin_education_admission', 'viin_education_crm'],

    'data': [
        'views/crm_lead_views.xml',
        'views/education_admission_views.xml',
        'views/education_application_views.xml',
        ],

    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
