# -- coding: utf-8 --


from odoo import models, fields, api


class Tipoasignatura(models.Model):
    _name = 'upolang.tipoasignatura'  
    _description = 'Tipo Asignatura'

    name = fields.Char(string="Tipo de la Asignatura", size=40, required=True)
    idAsignatura = fields.One2many('upolang.asignatura','idTipoAsignatura', string='Tipo de asignaturas')
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))  
        return result
    