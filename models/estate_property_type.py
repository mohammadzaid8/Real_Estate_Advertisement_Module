from odoo import fields,models

class PropertyType(models.Model):
    _name="estate_property_type"

    name = fields.Char(required=True)

    _sql_constraints = [
        ('unique_name','UNIQUE(name)','This Property Type is Already Exists!!!')
    ]