from odoo import models, fields, api

class Metodopago(models.Model):

    _name = 'upolang.metodopago'
    _description = 'Metodo de pago'

    
    descripcion = fields.Char(string="Descripción")
    idFactura = fields.One2many('upolang.factura','idAlumno', string='Facturas')
    idPago = fields.One2many('upolang.pago', 'idTipoPago', string='Pagos')
    
    # Esto es para que cuando selecciones el método de pago en pagos aparezca la descripcion del metodo de pago
    def name_get(self):
        """
        Personaliza cómo se muestra el registro en campos Many2one.
        Aquí se usa el valor del campo 'descripcion' directamente.
        """
        result = []
        for record in self:
            # El formato mostrado será la descripción
            result.append((record.id, record.descripcion))
        return result
    