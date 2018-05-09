from odoo import api,fields,models


class sale(models.Model):
    _inherit='sale.order'

    payment_mode = fields.Selection([
        ('cash', 'Cash On Delivery'),
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
        ('netbanking', 'Net Benking'),
        ('check', 'Check'),
        ], string='Payment Mode', default='cash')

    dist_name = fields.Char('Distributor Name')

    @api.multi
    def action_print(self):
        print "HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        rec=self.env['res.partner'].search([('name','=','Agrolait')])
        print 'recccccccccccccc',rec
        self.partner_id=rec.id