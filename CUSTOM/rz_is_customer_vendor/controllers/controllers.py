# -*- coding: utf-8 -*-
# from odoo import http


# class RzIsCustomerVendor(http.Controller):
#     @http.route('/rz_is_customer_vendor/rz_is_customer_vendor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rz_is_customer_vendor/rz_is_customer_vendor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rz_is_customer_vendor.listing', {
#             'root': '/rz_is_customer_vendor/rz_is_customer_vendor',
#             'objects': http.request.env['rz_is_customer_vendor.rz_is_customer_vendor'].search([]),
#         })

#     @http.route('/rz_is_customer_vendor/rz_is_customer_vendor/objects/<model("rz_is_customer_vendor.rz_is_customer_vendor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rz_is_customer_vendor.object', {
#             'object': obj
#         })
