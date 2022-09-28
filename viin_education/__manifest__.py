{
    'name': "Education Management Application",
	'name_vi_VN': "Phần mềm quản lý trường học",
    'summary': """
Application management Education""",
    'summary_vi_VN': """
Phần mềm quản lý trường học
""",

    'description': """
What it does
============

    
Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,
    'description_vi_VN': """
Ứng dụng này làm gì
===================


Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com/apps/app/15.0",
    'live_test_url': "https://v15demo-int.viindoo.vn",
    'live_test_url_vi_VN': "https://v15demo-vn.viindoo.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Education',
    'version': '0.1.0',
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/education_student_view.xml',
        'views/student_level_view.xml',
        'views/education_class_view.xml',
        'views/education_school_view.xml',
        'views/education_class_group_view.xml',
        'views/res_partner_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 45.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
