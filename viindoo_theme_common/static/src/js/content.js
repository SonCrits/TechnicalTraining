/** @odoo-module **/

import contentMenu from 'website.contentMenu';


contentMenu.PagePropertiesDialog.include({
    xmlDependencies: contentMenu.PagePropertiesDialog.prototype.xmlDependencies.concat(
        ['/viindoo_theme_common/static/src/xml/website.pageProperties.xml']
    ),
    _rpc: function () {
        if (arguments[0].model === 'website.page' && arguments[0].method === 'save_page_info')
            arguments[0].args[1].is_header_absolute = this.$('#is_header_absolute').prop('checked');
        return this._super(...arguments);
    }
});
