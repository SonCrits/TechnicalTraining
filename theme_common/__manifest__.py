{    'name': "Theme Common",
    'name_vi_VN': "Thiết kế Website",

    'summary': """
 Theme base, setting for website theme""",

    'summary_vi_VN': """
    Chủ đề cơ sở, cài đặt chung cho các chủ đề website
        """,

    'description': """

Editions Supported
==================
1. Community Edition

    """,

    'description_vi_VN': """

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v15demo-int.viindoo.com",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/Viindoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    'installable': True,
    'application': False,
    'auto_install': ['website'],
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
