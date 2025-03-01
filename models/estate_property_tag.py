from odoo import fields,models


class PropertyTag(models.Model):
    _name="estate_property_tag"
    _order="name"
    _description="This is property tag section"
    _sql_constraints =[
        ('unique_name','UNIQUE(name)','This Property Tag is Already Exists!!')   
    ]

    name = fields.Char(required = True)
    color = fields.Integer(string='color')
