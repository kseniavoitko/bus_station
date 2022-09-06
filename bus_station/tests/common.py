from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_bus_user = self.env.ref(
            'bus_station.group_bus_user')
        self.group_bus_admin = self.env.ref(
            'bus_station.group_bus_admin')
        self.bus_user = self.env['res.users'].create({
            'name': 'Bus User',
            'login': 'bus_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_bus_user.id)],
        })
        self.bus_admin = self.env['res.users'].create({
            'name': 'Bus Admin',
            'login': 'bus_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_bus_admin.id)],
        })
        self.station_demo = self.env['bus.station'].create({
            'name': 'Demo Station',
            'city': 'Demo City'})
