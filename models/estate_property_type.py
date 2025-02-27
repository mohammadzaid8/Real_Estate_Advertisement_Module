from odoo import fields,models,api

class PropertyType(models.Model):
    _name="estate_property_type"
    _order="name"
    _description="This is property Type section"
    _sql_constraints = [
        ('unique_name','UNIQUE(name)','This Property Type is Already Exists!!!')
    ]

    name = fields.Char(required=True)
    sequence = fields.Integer(store=True , default = 0)

    property_ids = fields.One2many('estate_property','property_type_id',string="Properties")
    offer_ids = fields.One2many('estate_property_offer','property_type_id',string="Offers")
    offer_count = fields.Integer(compute="_compute_offer_count",string="Total Count of offers")

    property_count = fields.Integer(compute="_compute_property_count",string="Total Count of properties")

    @api.depends('property_ids')
    def _compute_property_count(self):
        for record in self:
            record.property_count = self.env['estate_property'].search_count([('property_type_id', '=', record.id)])

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)