# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rz_contact_custom(models.Model):
#     _name = 'rz_contact_custom.rz_contact_custom'
#     _description = 'rz_contact_custom.rz_contact_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
