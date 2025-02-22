from odoo import fields,models,api
from odoo.tools import date_utils 

from datetime import datetime,timedelta,date
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name="estate_property_offer"

    price = fields.Float()
    status = fields.Selection([('Accepted','Accepted'),('Refused','Refused')],copy = False)
    validity = fields.Integer(string="Validity",default=7)
    date_deadline = fields.Date(string="Date Of DeadLine", store=True,compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    partner_id = fields.Many2one('res.partner',string = "Partners",required=True)
    property_id = fields.Many2one('estate_property',string="Property Name",required = True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days = record.validity)
            else:
                record.date_deadline = date.today() + timedelta(days = record.validity)

    @api.onchange('date_deadline')
    def _inverse_date_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else date.today()
            record.validity = (record.date_deadline - create_date).days
        
    def buyer_conform(self):
        for record in self:
            record.status = 'Accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

    def cancel_buyer(self):
        for record in self:
            record.status = 'Refused'

            accepted_offers = self.env['estate_property_offer'].search([('status', '=', 'Accepted')])

            if not accepted_offers:
                record.property_id.selling_price = 0.0

            
    _sql_constraints = [
       ('Check_price','CHECK(price >= 0)','An Offer Price Must be Positive')
    ]

    # @api.constrains('property_id')
    # def check_price(self):
    #     for record in self:
    #         if record.property_id.selling_price:
    #             if record.property_id.selling_price < ((record.property_id.expected_price) * 9) / 10:
    #                 raise ValidationError("The Selling Price must be grater than 90% of expected price")