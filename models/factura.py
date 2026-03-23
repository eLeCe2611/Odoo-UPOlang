# -- coding: utf-8 --


from odoo import models, fields, api


class Factura(models.Model):
    _name = 'upolang.factura'  
    _description = 'Factura'

    fecha = fields.Date(string="Fecha", required=True)
    total = fields.Integer(string="Total", required=True)
    estado = fields.Char(string="Estado", required=True)
    idAlumno = fields.Many2one('upolang.alumno', string="Alumno", required=True)
    idMatricula = fields.Many2one('upolang.matricula', string="Matrícula Asociada", ondelete='set null')
    idPago = fields.Many2one('upolang.pago', string="Pago", required=True)
    
    def name_get(self):
        """
        Devuelve una cadena con la fecha y el total de la factura cuando se selecciona en un campo Many2one.
        """
        result = []
        for record in self:
            # Combinar la fecha y el total de la factura
            display_name = f"Total: {record.total}€ - Fecha {record.fecha}"  # Se puede personalizar el formato
            result.append((record.id, display_name))  # Devuelve la combinación como nombre del registro
        return result
    
    