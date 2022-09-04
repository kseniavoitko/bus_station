from datetime import datetime
from odoo import models, fields, api


class BusTimetable(models.Model):
    _name = 'bus.timetable'
    _description = 'Bus Timetable'

    # name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    route_id = fields.Many2one(comodel_name='bus.route', string='Route', required=True)
    driver_id = fields.Many2one(comodel_name='res.partner', string='Driver', required=True)
    transport_id = fields.Many2one(comodel_name='bus.transport', string='Transport', required=True)
    bus_number = fields.Char(related='transport_id.bus_number')
    seats = fields.Integer(related='transport_id.seats')
    departure_datetime = fields.Datetime(string='Departure Date', required=True)
    arrival_datetime = fields.Datetime(string='Arrival Date', required=True)
    # duration_time = fields.Float(compute="_compute_duration_time", store=True)

    # @api.depends('departure_datetime', 'arrival_datetime')
    # def _compute_duration_time(self):
    #     for rec in self:
    #         if rec.arrival_datetime and rec.departure_datetime:
    #             rec.duration_time = rec.arrival_datetime - rec.departure_datetime

    def name_get(self):
        """ Display 'route_id' """
        res = []
        for timetable in self:
            name = timetable.route_id
            res.append((timetable.id, name))
        return res
