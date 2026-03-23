# -- coding: utf-8 --


from odoo import models, fields, api


class Pago(models.Model):
    _name = 'upolang.pago'  
    _description = 'Pago'

    fecha = fields.Date(string="Fecha", required=True)
    descuento = fields.Boolean(string="Descuento")
    efectivo = fields.Float(string="Efectivo")
    numTarjeta = fields.Integer(string="Número Tarjeta")
    numPaypal = fields.Integer(string="Número Paypal")
    idFactura = fields.Many2one('upolang.factura', string='Factura')
    idTipoPago = fields.Many2one('upolang.metodopago', string='Metodo de pago')
    idFactura = fields.Many2one('upolang.factura', string="Factura", required=True)
    
    