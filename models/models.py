# -*- coding: utf-8 -*-

from odoo import models, fields, api

class do_luarprop(models.Model):
    _inherit = 'stock.picking'

    delivery_status = fields.Selection([('kirim','Kirim'),('kembali','Kembali'),('done','Done')],'Delivery Status')
    jml_kembali = fields.Char("Return Quantity")
    tgl_kembali = fields.Date()






