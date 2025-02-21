from odoo import fields,models,api
from odoo.tools import date_utils

class Property(models.Model):
    _name = 'estate_property'
    _description='This table for estate property'


    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Integer()
    date_availability = fields.Date(copy = False, default = date_utils.add(fields.Date.today(),months =3))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True,copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('East','East'),('West','West'),('North','North'),('south','South')
    ])
    active = fields.Boolean(default = False)
    state = fields.Selection([
        ('New','New'),('Offer Received','Offer Received'),
        ('Offer Accepted','Offer Accepted'),('Sold','Sold'),
        ('Cancelled','Cancelled')],
        required = True,copy = False,default = 'New')

    property_type_id = fields.Many2one('estate_property_type',string="Property Type")
    seller_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer_id  = fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids = fields.Many2many('estate_property_tag',string="Property Tag")

    offer_ids = fields.One2many('estate_property_offer', 'property_id', string = "Offers for the sale")
    

    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price",default = 0)

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'))

