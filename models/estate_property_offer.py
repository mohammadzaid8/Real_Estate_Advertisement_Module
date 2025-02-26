from datetime import datetime,timedelta,date

from odoo import fields,models,api
from odoo.tools import date_utils 
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name="estate_property_offer"
    _order="price desc"
    _description="This is offer section"
    _sql_constraints = [
       ('Check_price','CHECK(price >= 0)','An Offer Price Must be Positive')
    ]

    price = fields.Float()
    status = fields.Selection([('Accepted','Accepted'),('Refused','Refused')],copy = False)
    validity = fields.Integer(string="Validity",default=7)
    date_deadline = fields.Date(string="Date Of DeadLine", store=True,compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    partner_id = fields.Many2one('res.partner',string = "Partners",required=True)
    property_id = fields.Many2one('estate_property',string="Property Name",required = True,ondelete='cascade')

    property_type_id = fields.Many2one('estate_property_type',related="property_id.property_type_id",store=True)


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
        

    def create(self, vals_list):
        for vals in vals_list:
            property_id = vals.get('property_id')

            if property_id:
                property_record = self.env['estate_property'].browse(property_id)

                if property_record.exists():
                    best_price = max(property_record.offer_ids.mapped('price'), default=0.0)

                    if vals.get('price', 0.0) <= best_price:
                        raise ValidationError("Your offer must be higher than the current best price!")

        return super().create(vals_list)
    
    def buyer_conform(self):
        for record in self:
            if record.property_id.state == 'Offer Accepted':
                raise ValidationError("Only Accept One Offer")
            else:
                record.status = 'Accepted'
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
                record.property_id.statusBarOfProperty = 'Offer Accepted'
                record.property_id.state='Offer Accepted'

    def cancel_buyer(self):
        for record in self:
            record.status = 'Refused'

            accepted_offers = self.env['estate_property_offer'].search([('status', '=', 'Accepted')])

            if not accepted_offers:
                record.property_id.selling_price = 0.0
                record.property_id.statusBarOfProperty = 'Offer Received'

