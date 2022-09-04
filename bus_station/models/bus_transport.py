from odoo import models, fields, api


class BusTransport(models.Model):
    _name = 'bus.transport'
    _description = 'Bus Transport'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    bus_number = fields.Char(required=True)
    seats = fields.Integer(required=True)
