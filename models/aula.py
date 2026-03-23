from odoo import models, fields, api


class Aula(models.Model):
    _name = 'upolang.aula'  
    _description = 'Aula'

    # edificio, planta, numAula, capacidad
    direccion = fields.Char(string="Dirección", size=40, required=True)
    edificio = fields.Integer(string="Edificio", required=True)
    planta = fields.Integer(string='Planta',required=True)
    numAula = fields.Integer(string='NumAula',required=True)
    capacidad = fields.Integer(string="Capacidad", required=True)
    idAsignaturas = fields.One2many("upolang.asignatura",'idAula',string='Asignaturas')
    
    def name_get(self):
        """
        Devuelve una cadena legible para mostrar en los campos Many2one
        (por ejemplo: 'Edificio 1 - Aula 3').
        """
        result = []
        for record in self:
            name = f"Edificio {record.edificio} - Aula {record.numAula}"
            result.append((record.id, name))
        return result