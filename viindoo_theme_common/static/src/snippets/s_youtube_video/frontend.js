odoo.define('website.s_youtube_video', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');
    const core = require('web.core')

    const YoutubeVideo = publicWidget.Widget.extend({
        selector: '.s_youtube_video',
        xmlDependencies: ['/viindoo_theme_common/static/src/xml/s_youtube_video.xml'],
        events: {
            'click .btn_youtube_play': '_onPopupVideo'
        },

        _onPopupVideo: function (event) {
            const $youtubePopup = $(core.qweb.render('s_video_youtube_modal', {
                videoId: this.el.dataset.videoId
            }));
            
            $youtubePopup.appendTo('body');
            $youtubePopup.modal().on('hidden.bs.modal', () => $youtubePopup.remove());
        },
        /**
         * @override
         */
        destroy: function () {
            this._super.apply(this, arguments);
        }
    });
    publicWidget.registry.youtubeVideo = YoutubeVideo;

    return YoutubeVideo;

});
