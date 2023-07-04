# -*- coding: utf-8 -*-
# from odoo import http


# class Radio(http.Controller):
#     @http.route('/radio/radio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/radio/radio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('radio.listing', {
#             'root': '/radio/radio',
#             'objects': http.request.env['radio.radio'].search([]),
#         })

#     @http.route('/radio/radio/objects/<model("radio.radio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('radio.object', {
#             'object': obj
#         })
