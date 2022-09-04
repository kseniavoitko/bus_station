from odoo import models, fields, api


class BusDriver(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(default=True)
