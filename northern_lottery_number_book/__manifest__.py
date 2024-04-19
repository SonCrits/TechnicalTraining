{
    'name': "Northern Lottery Number Book",
    'name_vi_VN': "Sổ số miền Bắc",

    'summary': """
Lottery Ticket Management Software
""",

    'summary_vi_VN': """
Phần mềm quản lý ghi sổ số
""",

    'description': """
What it does
============

Key Features
============

Editions Supported
==================
1. Community Edition
2. Enterprise Edition
    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================

Tính năng chính
===============

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise
    """,

    'author': "Soncrits",
    # 'website': "https://viindoo.com/apps/app/16.0/viin_crm_dob",
    # 'live_test_url': "https://v16demo-int.viindoo.com",
    # 'live_test_url_vi_VN': "https://v16demo-vn.viindoo.com",
    # 'demo_video_url': "https://youtu.be/RDcBKJ4gCFA",
    # 'support': "apps.support@viindoo.com",

    'category': 'Hidden',
    'version': '0.0.1',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/daily_predition_views.xml',
    ],
    'images': [
        'static/description/main_screenshot.png'
        ],
    'installable': True,
    'application': True,
    'price': 18.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
