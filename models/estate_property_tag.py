from odoo import fields,models


class PropertyTag(models.Model):
    _name="estate_property_tag"
    _order="name"

    name = fields.Char(required = True)
    color = fields.Integer(string='color')

    _sql_constraints =[
        ('unique_name','UNIQUE(name)','This Property Tag is Already Exists!!')   
    ]