# -*- coding: utf-8 -*-
from odoo import http

# class PosQrCode(http.Controller):
#     @http.route('/pos_qr_code/pos_qr_code/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_qr_code/pos_qr_code/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_qr_code.listing', {
#             'root': '/pos_qr_code/pos_qr_code',
#             'objects': http.request.env['pos_qr_code.pos_qr_code'].search([]),
#         })

#     @http.route('/pos_qr_code/pos_qr_code/objects/<model("pos_qr_code.pos_qr_code"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_qr_code.object', {
#             'object': obj
#         })