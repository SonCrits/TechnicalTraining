from lxml import etree
from odoo import api, SUPERUSER_ID


# We add the data-snippet attribute on the sections of old page views that were used in v13 to be able to use the save
# snippet feature in v14.
def _add_snippet_key(env):
    page_views = env['ir.ui.view'].search(
        [('arch_db', 'ilike', '<div id="wrap"'),
         ('mode', '=', 'primary'),
         ('type', '=', 'qweb')])
    for view in page_views:
        arch_tree = etree.fromstring(view.arch_db)
        elements = arch_tree.xpath("//div[@id='wrap']//section[@data-name][not(@data-snippet)]")
        for el in elements:
            el.set('data-snippet', 's_' + '_'.join(el.attrib.get(
                'data-name', 'Unknown Snippet').split(' ')).lower())
            view.write({
                'arch_db': env['ir.ui.view']._pretty_arch(arch_tree)
            })


def migrate(cr, installed_version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _add_snippet_key(env)
