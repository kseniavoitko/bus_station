from odoo import models, fields


class BusTimetable(models.Model):
    _name = 'bus.timetable'
    _description = 'Bus Timetable'

    active = fields.Boolean(
        default=True, )
    route_id = fields.Many2one(comodel_name='bus.route',
                               string='Route', required=True)
    driver_id = fields.Many2one(comodel_name='res.partner',
                                string='Driver', required=True,
                                domain=[('is_driver', '=', True)])
    transport_id = fields.Many2one(comodel_name='bus.transport',
                                   string='Transport', required=True)
    bus_number = fields.Char(related='transport_id.bus_number')
    seats = fields.Integer(related='transport_id.seats')
    departure_datetime = fields.Datetime(string='Departure Date',
                                         required=True)
    arrival_datetime = fields.Datetime(string='Arrival Date',
                                       required=True)
    qty = fields.Integer(default=1)

    def name_get(self):
        """ Display 'route_id' """
        res = []
        for timetable in self:
            name = timetable.route_id
            res.append((timetable.id, name))
        return res
