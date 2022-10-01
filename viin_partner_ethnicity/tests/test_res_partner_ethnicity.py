from psycopg2 import IntegrityError

from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged('post_install', '-at_install')
class TestPartnerEthnicity(TransactionCase):

    def setUp(self):
        super(TestPartnerEthnicity, self).setUp()
        self.country_id = self.ref('base.vn')
        self.ethnicity_1 = self.env['res.partner.ethnicity'].create({
            'code': '001',
            'name': 'Xơ đăng',
            'country_id': self.country_id
            })
        
        self.ethnicity_2 = self.env['res.partner.ethnicity'].create({
            'code': '002',
            'name': 'Mnông',
            'country_id': self.country_id
            })
        
    def test_11_sql_constraints(self):
        # Check constraints when creating a ethnicity
        with self.assertRaises(IntegrityError), mute_logger('odoo.sql_db'):
            self.ethnicity_3 = self.env['res.partner.ethnicity'].create({
            'code': '001',
            'name': 'Xơ đăng',
            'country_id': self.country_id
            })
        
    def test_12_sql_contraints(self):
        # Check constraints when updating a ethnicity
        with self.assertRaises(IntegrityError), mute_logger('odoo.sql_db'):
            self.ethnicity_2.write({'code': '001'})
            self.ethnicity_2.flush()
            
    def test_21_method_copy(self):
        self.assertTrue( self.ethnicity_1.copy(), "Copy ethnicity to fail")
