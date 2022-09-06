from odoo import models, fields


class CreateTimetableLineWizard(models.TransientModel):
    _name = 'create.timetable.line.wizard'
    _description = 'Create timetable'

    departure_datetime = fields.Datetime(string='Departure Date',
                                         required=True)
    arrival_datetime = fields.Datetime(string='Arrival Date',
                                       required=True)


class CreateTimetableWizard(models.TransientModel):
    """Create timetables for one driver, route and transport
    in line write departure_datetime and arrival_datetime
    """
    _name = 'create.timetable.wizard'
    _description = 'Create timetable'

    def default_route(self):
        return self.env['bus.route'].browse(self._context.get('active_id'))

    driver_id = fields.Many2one('res.partner', string='Driver',
                                required=True,
                                domain=[('is_driver', '=', True)])
    route_id = fields.Many2one(comodel_name='bus.route',
                               string='Route', required=True,
                               default=default_route)
    transport_id = fields.Many2one(comodel_name='bus.transport',
                                   string='Transport', required=True)
    line_ids = fields.Many2many('create.timetable.line.wizard')

    def action_create(self):
        for rec in self:
            for line in self.line_ids:
                self.env['bus.timetable'].create({
                    'driver_id': rec.driver_id.id,
                    'route_id': rec.route_id.id,
                    'transport_id': rec.transport_id.id,
                    'departure_datetime': line.departure_datetime,
                    'arrival_datetime': line.arrival_datetime,
                })
