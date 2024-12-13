# -*- coding: utf-8 -*-
# from odoo import http


# class Owl17(http.Controller):
#     @http.route('/owl_17/owl_17', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_17/owl_17/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_17.listing', {
#             'root': '/owl_17/owl_17',
#             'objects': http.request.env['owl_17.owl_17'].search([]),
#         })

#     @http.route('/owl_17/owl_17/objects/<model("owl_17.owl_17"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_17.object', {
#             'object': obj
#         })

