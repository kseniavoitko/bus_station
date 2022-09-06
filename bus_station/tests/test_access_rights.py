from odoo.addons.school_lesson_6_4.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'bus_station', 'access')
class TestAccessRights(TestCommon):

    def test_01_bus_user_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['bus.station'].with_user(self.bus_user).create(
                {'name': 'Test Station',
                 'city': 'Test City'})
        with self.assertRaises(AccessError):
            self.station_demo.with_user(self.bus_user).unlink()

    def test_02_bus_admin_access_rights(self):
        book = self.env['bus.station'].with_user(self.bus_admin).create(
            {'name': 'Test Station',
             'city': 'Test City'})
        book.with_user(self.bus_admin).read()
        book.with_user(self.bus_admin).write({
            'name': 'Test Station 2',
            'city': 'Test City 2'})
        book.with_user(self.bus_admin).unlink()
