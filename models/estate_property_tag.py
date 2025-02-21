from odoo import fields,models

class PropertyTag(models.Model):
    _name="estate_property_tag"

    name = fields.Char(required = True)
