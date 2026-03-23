# -- coding: utf-8 --


from odoo import models, fields, api


class Matricula(models.Model):
    _name = 'upolang.matricula'  
    _description = 'Matricula'

    precio = fields.Float(string="Precio")
    fechaInicio = fields.Date(string="Fecha inicio", required=True)
    fechaFin = fields.Date(string="Fecha fin", required=True)
    idAlumno = fields.Many2one('upolang.alumno', string="Alumno", required=True)
    idAsignatura = fields.Many2one('upolang.asignatura', string="Asignatura", required=True)
    idFactura = fields.Many2one('upolang.factura', string="Factura")
    
    def name_get(self):
        """
        Devuelve el nombre del alumno y la asignatura (idioma + nivel) cuando se seleccionan en los campos Many2one.
        """
        result = []
        for record in self:
            alumno_nombre = record.Alumno.nomAlumno  # Obtener el nombre del alumno
            asignatura_nombre = f"{record.Asignatura.idioma} - {record.Asignatura.nivel}"  # Combinar idioma y nivel
            display_name = f"{alumno_nombre} - {asignatura_nombre}"  # Combina nombre del alumno y asignatura
            result.append((record.id, display_name))  # Devuelve la combinación como nombre del registro
        return result