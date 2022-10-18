{    'name': "Theme Viindoo Common",
    'name_vi_VN': "Thiết kế Website với thương hiệu Viindoo",

    'summary': """
 Theme base, colors, styles, librarys for Theme Viindoo""",

    'summary_vi_VN': """
    Chủ đề cơ sở, màu sắc, thư viện cho website với thương hiệu Viindoo
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
    # Check https://github.com/Viindoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'data/attachment_data.xml',
        # Snippets
        'views/snippets/s_card_column_img_text_header.xml',
        'views/snippets/s_viindoo_mega_menu.xml',
        'views/snippets/s_erponline_mega_menu.xml',
        'views/snippets/s_viindoo_services.xml',
        'views/snippets/s_solutions_video.xml',
        'views/snippets/s_solution_landing_page.xml',
        'views/snippets/s_viindoo_landingpage_utilities.xml',
        'views/snippets/s_youtube_video.xml',
        'views/snippets/snippets.xml',
        'views/website_templates.xml',
        'views/website_views.xml'
    ],
    'assets': {
        'web._assets_frontend_helpers': [
            'viindoo_theme_common/static/src/scss/variables.scss',
            'viindoo_theme_common/static/src/scss/mixins.scss',
        ],
        'web.assets_frontend': [
            # SCSS
            'viindoo_theme_common/static/src/scss/fontello-embedded.css',
            'viindoo_theme_common/static/src/scss/viin_theme_common.scss',
            'viindoo_theme_common/static/src/scss/viindoo.scss',

            # Legacy
            'viindoo_theme_common/static/src/scss/legacy/s_trial_cta.scss',
            'viindoo_theme_common/static/src/scss/legacy/s_customer_rate.scss',
            'viindoo_theme_common/static/src/scss/legacy/s_implementation_steps.scss',
            'viindoo_theme_common/static/src/scss/legacy/s_header_page.scss',
            'viindoo_theme_common/static/src/scss/legacy/s_guideline_apps.scss',

            # JS
            'viindoo_theme_common/static/src/js/top_menu.js',
        ],
        'website.assets_editor': [
            'viindoo_theme_common/static/src/js/content.js',
        ],
        'web_editor.assets_wysiwyg': [
            'viindoo_theme_common/static/src/js/fonts.js',
        ]
    },
    'images': [
    	# 'static/description/main_screenshot.png'
    	],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
