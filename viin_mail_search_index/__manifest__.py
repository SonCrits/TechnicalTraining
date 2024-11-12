{
    'name': "Messages Search & Filter",
    'name_vi_VN': "Tìm kiếm và lọc tin",

    'summary': """Search and filter messages in Discuss app""",
    'summary_vi_VN': """Tìm kiếm và lọc tin nhắn trong ứng dụng Thảo luận
""",

    'description': """
Demo video: `Messages Search & Filter <https://youtu.be/gM0PQqmPzNM>`_

Problem
=======

Search bar in Discuss app has been removed since Odoo 15. This brings a lot of difficulty for users to track their communication history.

Key features
============

Messages Search & Filter module add the search bar in the Discuss app. This feature allow user:

* Search for the discussed content on the Search bar with the needed criteria
* Filter the content with other criteria such as Has Mentioned, Need Action, etc.

Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Demo video: `Tìm kiếm và lọc tin <https://youtu.be/gM0PQqmPzNM>`_

Vấn đề
======

Hộp tìm kiếm tin nhắn/thông điệp đã bị gỡ bỏ ở Odoo 15, gây ra nhiều khó khăn cho người dùng khi muốn tra cứu lại lịch sử trao đổi, thông tin liên lạc.

Tính năng nổi bật
=================

Mô-đun Tìm kiếm và lọc tin cung cấp thêm hộp tìm kiếm ở ứng dụng Thảo luận. Tính năng này cho phép người dùng:

* Tìm kiếm nội dung đã trao đổi với những tiêu chí cần thiết trên thanh tìm kiếm
* Bộ lọc tìm kiếm nội dung theo một số tiêu chí khác như Có đề cập, Cần có hành động, v.v.

Ấn bản được hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v16demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v16demo-vn.viindoo.com",
    'demo_video_url': "https://youtu.be/gM0PQqmPzNM",
    'support': "apps.support@viindoo.com",
    'category': 'Productivity/Discuss',
    'version': '0.1.0',
    'depends': ['mail'],
    'data': [
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'assets': {
        'web.assets_backend': [
            'viin_mail_search/static/src/components/*/*.js',
            'viin_mail_search/static/src/components/*/*.xml',
            'viin_mail_search/static/src/models/*.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 45.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
