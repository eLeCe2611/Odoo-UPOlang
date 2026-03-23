# -- coding: utf-8 --


from odoo import models, fields, api


class Progreso(models.Model):
    _name = 'upolang.progreso'  
    _description = 'Progreso'

    fecha  = fields.Date(string="Fecha", required=True)
    estado = fields.Integer(string="Estado")
    idAsignatura = fields.Many2one('upolang.asignatura', string='Asignatura', required=True)          
    idAlumno = fields.Many2one('upolang.alumno', string='Alumno', required=True)          
    