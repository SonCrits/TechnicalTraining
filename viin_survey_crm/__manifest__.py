{
    'name': "Survey - CRM",
    'name_vi_VN': "Khảo sát - CRM",

    'summary': """
    Integrated Survey With CRM
""",
    'summary_vi_VN': """
    Tích hợp khảo sát với CRM""",

    'description': """
What it does
============
* Link Lead to Survey

Key Features
============
* Link Lead to Survey
* Automatically generate Lead after submitting Survey form

Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
* Liên kết Tiềm năng với Khảo sát

Tính năng nổi bật
=================
* Liên kết Tiềm năng với Khảo sát
* Tự động tạo Tiềm năng khi nộp form Khảo sát

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Sales/CRM',
    'version': '0.1.0',
    'depends': ['crm', 'survey'],

    'data': [
        'views/survey_survey_views.xml',
        'views/survey_question_views.xml',
        'views/crm_lead_views.xml'
        ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
