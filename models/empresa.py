# -- coding: utf-8 --


from odoo import models, fields, api


class Empresa(models.Model):
    _name = 'upolang.empresa'  
    _description = 'Empresa'

    name = fields.Char(string="Nombre de la Empresa", size=40, required=True)
    telefono = fields.Char(string="Teléfono")
    idContrato = fields.One2many('upolang.contrato','idEmpresa', string='Contratos')
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.name))  # Devuelve el nombre de la empresa en lugar del ID
        return result