# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'upolang.profesor'
    _description = 'Upolang Profesor'

    name = fields.Char(string="Nombre", required=True)
    telefono = fields.Char(string="Teléfono")
    correo = fields.Char(string="Correo Electrónico")
    idContrato = fields.One2many('upolang.contrato','idProfesor', string='Contratos')
    
    def name_get(self):
        result = []
        for record in self:
            display_name = f"{record.name} ({record.id})"  # Formato deseado con nombre e ID
            result.append((record.id, display_name))
        return result
    
