from odoo import models, fields, api


class BusRoute(models.Model):
    _name = 'bus.route'
    _description = 'Bus Route'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    station_from_id = fields.Many2one(comodel_name='bus.station',
                                      string='From', required=True)
    station_to_id = fields.Many2one(comodel_name='bus.station',
                                    string='To', required=True)

    @api.onchange('station_from_id', 'station_to_id')
    def _onchange_station(self):
        if self.station_from_id and self.station_to_id:
            self.name = self.station_from_id.city + ', ' \
                + self.station_from_id.name + '-' \
                + self.station_to_id.city + ', ' \
                + self.station_to_id.name
