from odoo import models


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def button_uninstall(self):
        # Since this module is not a theme, removing it will
        # affect the themes that depend on it, as themes that
        # are not properly removed will lead to some unexpected
        # errors. So we need to remove all themes before uninstall
        # to avoid error.
        if 'viindoo_theme_common' in self.mapped('name'):
            theme_deps = self.downstream_dependencies().filtered(lambda m: m.name.startswith('theme_'))
            websites = self.env['website']
            for theme in theme_deps:
                websites |= theme._theme_get_stream_website_ids()
            for website in websites:
                self._theme_remove(website)
        return super().button_uninstall()
