# -*- coding: utf-8 -*-
# from odoo import http


# class RzContactCustom(http.Controller):
#     @http.route('/rz_contact_custom/rz_contact_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rz_contact_custom/rz_contact_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rz_contact_custom.listing', {
#             'root': '/rz_contact_custom/rz_contact_custom',
#             'objects': http.request.env['rz_contact_custom.rz_contact_custom'].search([]),
#         })

#     @http.route('/rz_contact_custom/rz_contact_custom/objects/<model("rz_contact_custom.rz_contact_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rz_contact_custom.object', {
#             'object': obj
#         })
