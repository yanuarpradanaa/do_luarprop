# -*- coding: utf-8 -*-
from odoo import http

# class DoLuarprop(http.Controller):
#     @http.route('/do_luarprop/do_luarprop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/do_luarprop/do_luarprop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('do_luarprop.listing', {
#             'root': '/do_luarprop/do_luarprop',
#             'objects': http.request.env['do_luarprop.do_luarprop'].search([]),
#         })

#     @http.route('/do_luarprop/do_luarprop/objects/<model("do_luarprop.do_luarprop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('do_luarprop.object', {
#             'object': obj
#         })