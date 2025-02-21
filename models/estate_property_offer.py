from odoo import fields,models,api
from odoo.tools import date_utils 

class PropertyOffer(models.Model):
    _name="estate_property_offer"

    price = fields.Float()
    status = fields.Selection([('Accepted','Accepted'),('Refused','Refused')],copy = False)
    validity = fields.Integer(string="Validity",default=7)
    date_deadline = fields.Date(string="Date Of DeadLine",compute="_compute_date_deadline",inverse="_reverse_date_deadline")

    partner_id = fields.Many2one('res.partner',string = "Partners",required=True)
    property_id = fields.Many2one('estate_property',string="Property Name",required = True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = date_utils.add(fields.Date.today(), days = record.validity)

    # def _reverse_date_deadline(self):
    #     for record in self:
    #         record.validity = 5
   