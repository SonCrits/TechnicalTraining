odoo.define('viindoo_theme_common.wysiwyg.fonts', function(require) {
	const { fontIcons } = require('wysiwyg.fonts');

	fontIcons.push({ base: 'fa', parser: /\.(icon-viin-(?:\w|-)+)::?before/i });
});
