# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Alumno(models.Model):
    _name = 'upolang.alumno'
    _description = 'Alumnos'
    
    nomAlumno = fields.Char(string="Nombre del alumno", size=40, required=True)
    dni = fields.Char(string="DNI", size=40, required=True)
    domicilio = fields.Char(string="Domicilio", size=40, required=True)
    correo = fields.Char(string="Correo", size=40, required=True)
    localidad = fields.Char(string="Localidad", size=40, required=True)
    fechaNac = fields.Date('FNacimiento',required=True, autodate = True)
    idValoracion = fields.One2many('upolang.valoracion', 'idAlumno', string='Valoraciones')
    idEvaluacion = fields.One2many('upolang.evaluacion', 'idAlumno', string='Evaluaciones')
    idCertificado = fields.One2many('upolang.certificado','idAlumno', string='Certificados')
    idProgreso = fields.One2many('upolang.progreso','idAlumno', string='Progresos')
    idMatricula = fields.One2many('upolang.matricula','idAlumno', string='Matriculas')
    idFactura = fields.One2many('upolang.factura','idAlumno', string='Facturas')
    
    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            if len(self.dni) != 9 or not self.dni[:-1].isdigit() or not self.dni[-1].isalpha():
                return {
                    'warning': {
                        'title': "DNI inválido",
                        'message': "El DNI debe tener exactamente 8 dígitos seguidos de una letra.",
                    },
                }
                
    @api.onchange('fecha_nacimiento')
    def _onchange_fecha_nacimiento(self):
        if self.fecha_nacimiento:
            fecha_nacimiento = fields.Datetime.from_string(self.fecha_nacimiento)
            today = datetime.now().date()
            age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

            if fecha_nacimiento.date() > today:
                return {
                    'warning': {
                        'title': "Fecha de Nacimiento Inválida",
                        'message': "La fecha de nacimiento no puede ser posterior al día actual.",
                    },
                }
            if age < 18:
                return {
                    'warning': {
                        'title': "Fecha de Nacimiento Inválida",
                        'message': "Debe tener al menos 18 años.",
                    },
                }
                
    def name_get(self):
        """
        Devuelve el nombre y el DNI del alumno cuando se selecciona en un campo Many2one
        """
        result = []
        for record in self:
            display_name = f"{record.nomAlumno} ({record.dni})"  # Combina el nombre y el DNI
            result.append((record.id, display_name))  # Devuelve la combinación como nombre del registro
        return result