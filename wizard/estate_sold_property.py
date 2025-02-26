from odoo import fields, models,api

class EstateSoldProperty(models.TransientModel):
    _name = 'estate.sold.property.wizard'
    _description = 'Real Estate Sold Property'

    def getDataFromEstateProperty(self):
        return self.env['estate_property'].search([('state', '=', 'Sold')])
    
    property_ids = fields.Many2many(
        'estate_property',
        string='Sold Properties',
        default=getDataFromEstateProperty
    )


