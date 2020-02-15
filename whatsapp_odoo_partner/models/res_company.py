# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    _description = "Whatsapp"
    token_whatsapp = fields.Char('Token', help="Token to conect to Whatsapp.", copy=False)
