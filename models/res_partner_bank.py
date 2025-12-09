# -*- coding: utf-8 -*-

from odoo import models, fields


class MotsoftResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    description = fields.Char(string="Descripción", readonly=False, help="Característica descriptiva de la cuenta")
