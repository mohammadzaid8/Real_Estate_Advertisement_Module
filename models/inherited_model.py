from odoo import fields,models,api

class InheratedProperty(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate_property','seller_id',string="Inherent Salesperson",domain=['|',('state','=','New'),('state','=','Offer Received')])