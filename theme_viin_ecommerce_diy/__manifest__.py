{
    'name': "DIY Ecommerce Viindoo Theme",
    'name_vi_VN': "DIY Ecommerce Viindoo Theme",

    'summary': """
     Ecommerce Theme technical tools stores
""",
    'summary_vi_VN': """
    Cửa hàng công cụ kỹ thuật Chủ đề thương mại điện tử
""",

    'description': """
Ecommerce themes for technical tools stores
============
This theme will change color navigate bar, buttton, logo, ...


Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
Themes Ecommerce dành cho cửa hàng bán dụng cụ kỹ thuât


Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

""",

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v15demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v15demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    'category': 'Theme/Ecommerce',
    'version': '0.1',

    'depends': ['website_sale', 'viindoo_theme_common'],

    # always loaded
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        # Snippets
        'views/snippets/s_banner.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_process_steps.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_media_list.xml',
    ],
    'images': [
        'static/description/theme_viin_ecommerce_diy_preview.jpg',
    ],    
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
