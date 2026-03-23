from odoo import models, fields, api

class Evaluacion(models.Model):
    _name = 'upolang.evaluacion'  
    _description = 'Evaulacion'

    # fecha, descripcion, puntMaxima, puntObtenida
    fecha = fields.Date(string='Fecha',required=True)
    descripcion = fields.Text(string="Descripción")
    puntMaxima = fields.Float(string='Puntuacion maxima',required=True)
    puntObtenida = fields.Float(string="Puntuacion obtenida", required=True)
    idAsignatura = fields.Many2one('upolang.asignatura', string='Asignatura')
    idAlumno = fields.Many2one('upolang.alumno', string='Alumno', required=True)

    @api.constrains('puntObtenida')
    def _check_nota_examen(self):
        for record in self:
            if record.puntObtenida < 0 or record.puntObtenida > 10:
                raise models.ValidationError("La nota del examen debe estar entre 0 y 10.")