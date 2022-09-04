from odoo import models, fields, api


class BusRoute(models.Model):
    _name = 'bus.route'
    _description = 'Bus Route'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    station_from_id = fields.Many2one(comodel_name='bus.station', string='From', required=True)
    station_to_id = fields.Many2one(comodel_name='bus.station', string='To', required=True)

    def name_get(self):
        """ Display 'station_from_id-station_to_id' """
        res = []
        for field in self:
            name = str(field.station_from_id) + '-' + str(field.station_to_id)
            res.append((field.id, name))
        return res
