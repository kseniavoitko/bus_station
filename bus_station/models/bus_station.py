from odoo import models, fields, api


class BusStation(models.Model):
    _name = 'bus.station'
    _description = 'Bus Station'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    city = fields.Char(required=True)

    def name_get(self):
        """ Display 'city name' """
        res = []
        for field in self:
            name = field.city + ' ' + field.name
            res.append((field.id, name))
        return res
