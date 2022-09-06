from odoo import models, fields, _


class CreateTimetableLineWizard(models.TransientModel):
    _name = 'create.timetable.line.wizard'
    _description = 'Create timetable'

    departure_datetime = fields.Datetime(string='Departure Date', required=True)
    arrival_datetime = fields.Datetime(string='Arrival Date', required=True)


class CreateTimetableWizard(models.TransientModel):
    _name = 'create.timetable.wizard'
    _description = 'Create timetable'

    def default_route(self):
        return self.env['bus.route'].browse(self._context.get('active_id'))

    driver_id = fields.Many2one('res.partner', string='Driver', required=True)
    route_id = fields.Many2one(comodel_name='bus.route', string='Route', required=True, default=default_route)
    transport_id = fields.Many2one(comodel_name='bus.transport', string='Transport', required=True)
    line_ids = fields.Many2many('create.timetable.line.wizard')

    # def action_create(self):
    #     for record in self.line_ids:
    #         create()
