{
    'name': "Admission - Survey - CRM",
    'name_vi_VN': "Tuyển sinh - Khảo sát - CRM",

    'summary': """
    Admission, Survey and CRM Integration
""",
    'summary_vi_VN': """
    Tích hợp Tuyển sinh, Khảo sát, và CRM""",

    'description': """
What it does
============
The module connects Admission - CRM and Survey - CRM modules.

Key Features
============
* Link Survey to Admission.
* Update Admission on Lead when Lead is created from Survey.
    
Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
Mô đun này kết nối mô đun Tuyển sinh - CRM và mô đun Giáo dục - CRM.

Tính năng nổi bật
=================
* Liên kết Khảo sát tới Chương trình tuyển sinh.
* Cập nhật Chương trình tuyển sinh trên Tiềm năng khi Tiềm năng được tạo từ Khảo sát.
    
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
    'depends': ['viin_education_admission_crm', 'viin_survey_crm'],

    'data': [
        'views/survey_survey_views.xml',
        'views/education_admission_views.xml'
        ],

    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
