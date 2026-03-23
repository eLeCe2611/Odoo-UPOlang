# -*- coding: utf-8 -*-
# from odoo import http


# class UpolangApp(http.Controller):
#     @http.route('/upolang_app/upolang_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upolang_app/upolang_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upolang_app.listing', {
#             'root': '/upolang_app/upolang_app',
#             'objects': http.request.env['upolang_app.upolang_app'].search([]),
#         })

#     @http.route('/upolang_app/upolang_app/objects/<model("upolang_app.upolang_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upolang_app.object', {
#             'object': obj
#         })

