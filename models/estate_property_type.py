from odoo import fields,models

class PropertyType(models.Model):
    _name="estate_property_type"

    name = fields.Char(required=True)