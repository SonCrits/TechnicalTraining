{
    'name': "Contact Form - Source of Leads",
    'name_vi_VN': "Form Liên hệ - Nguồn của Tiềm năng",

    'summary': """
    Default Source for new leads created through the Contact Us Form
""",
    'summary_vi_VN': """
    Nguồn mặc định cho Tiềm năng mới được tạo thông qua Form Liên hệ""",

    'description': """
What it does
============
* Allow set default Source for new leads created through the Contact Us Form

Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô tả
=====
* Cho phép thiết lập Nguồn mặc định cho Tiềm năng mới được tạo thông qua Form Liên hệ

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Website/Website',
    'version': '0.1.0',
    'depends': ['website_crm'],

    'data': [
        'views/res_config_settings_views.xml'
        ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'subscription_price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
