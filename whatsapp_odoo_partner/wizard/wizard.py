# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError
import requests

class WhatsappSendMessage(models.TransientModel):

    _name = 'whatsapp.message.wizard'

    user_id = fields.Many2one('res.partner', string="Recipient")
    mobile = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="message", required=True)

    def send_message(self):
        if self.message and self.mobile:
            token = self.env.user.company_id.token_whatsapp
            if not token:
                raise ValidationError("Put the token in the company")
            else:
                params = {
                    "phone": self.mobile,
                    "body": self.message
                }
                response = requests.post(token, params=params)