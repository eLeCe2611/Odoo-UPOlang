# -- coding: utf-8 --


from odoo import models, fields, api


class Valoracion(models.Model):
    _name = 'upolang.valoracion'  
    _description = 'Valoracion'

    puntuacion = fields.Float(string='Puntuación')
    comentario = fields.Char(string='Comentario')
    fecha = fields.Date(string='Fecha',required=True)  
    idAlumno = fields.Many2one('upolang.alumno', string='Alumno', required=True)      
    idAsignatura = fields.Many2one('upolang.asignatura', string='Asignatura', required=True)          