# -- coding: utf-8 --


from odoo import models, fields, api

class Certificado(models.Model):
    _name = 'upolang.certificado'  
    _description = 'Certificado'
    
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string='Fecha',required=True)
    nivel = fields.Selection([('A1','A1'),
                              ('A2','A2'),
                              ('B1','B1'),
                              ('B2','B2')],
                              string='Nivel', required=True)
    
    idAlumno = fields.Many2one('upolang.alumno', string="Alumno", required=True)
    idAsignatura = fields.Many2one('upolang.asignatura', string="Asignatura", required=True, ondelete='cascade')    
