from odoo import fields,models,api

class ReadAndBrowseProperty(models.TransientModel):
    _name="estate.read.browse.property.wizard"

    input_id = fields.Integer(string="Enter id of search data",required=True,store=True)

    dataOfId = fields.Many2one('estate_property',string="Property Details",compute="_compute_data_from_id")
    property_ids = fields.Many2many('estate_property')


    @api.onchange('input_id')
    def _compute_data_from_id(self):
        for record in self:
            if record.input_id:
                data = self.env['estate_property'].browse(record.input_id)
                if data.exists():
                    record.dataOfId = data
                    record.property_ids = [(6,0,[data.id])]
                else:
                    record.dataOfId = False
                    record.property_ids = [(5,0,0)]
            else:
                record.dataOfId = False
                record.property_ids = [(5,0,0)]
