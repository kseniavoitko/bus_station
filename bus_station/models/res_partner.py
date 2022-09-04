from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(default=True)
