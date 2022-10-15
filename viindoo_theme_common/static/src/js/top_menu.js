odoo.define('viindoo_theme_common.top_menu_custom', function (require) {
    'use strict'

    const {Animation, registry} = require('website.content.snippets.animation');

    registry.topMenuCustom = Animation.extend({
        selector: '#wrapwrap',
        events: {
            'scroll': 'resetMenuExpanded'
        },
        start: function () {
            const $headerTop = $('header#top');
            const $megaMenu = $('#top_menu .o_mega_menu_toggle');

            $megaMenu.parent()
                .on('show.bs.dropdown', function (e) {
                    $headerTop.addClass('mega_opened');
                })
                .on('hide.bs.dropdown', function (e) {
                    $headerTop.removeClass('mega_opened');
                });
            return this._super(...arguments);
        },
        
        resetMenuExpanded: function () {
            $('header#top').removeClass('mega_opened');
            $('#top_menu .o_mega_menu_toggle').attr('aria-expanded', false);
            $('button.navbar-toggler').attr('aria-expanded', false);
        }
    });
});
