odoo.define('website.s_youtube_video_options', function (require) {
'use strict';

const options = require('web_editor.snippets.options');

options.registry.youtubeVideo = options.Class.extend({
    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------
    /**
     * @override
     */
    _computeWidgetState: function (methodName, params) {
        switch (methodName) {
            case 'videoId': {
                return this.$target.data('videoId')
            }
        }
        return this._super(...arguments);
    },
    /**
     * Sets the youtube video's ID.
     *
     * @see this.selectClass for parameters
     */
    videoId: function (previewMode, widgetValue, params) {
        this.$target.attr('data-video-id', widgetValue);
    },
});
});
