from odoo import models, fields


class BusStation(models.Model):
    _name = 'bus.station'
    _description = 'Bus Station'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    city = fields.Char(required=True)
    qty = fields.Integer(default=1)

    def name_get(self):
        """ Display 'city name' """
        res = []
        for field in self:
            name = field.city + ', ' + field.name
            res.append((field.id, name))
        return res
