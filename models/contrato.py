from odoo import models, fields, api


class Contrato(models.Model):
    _name = 'upolang.contrato'  
    _description = 'Contrato'

    # sueldo, detalles, fechainicio, fechafin
    sueldo = fields.Float(string="Sueldo", digits=(10, 2))
    fechaInicio = fields.Date(string='Fecha inicio',required=True)
    fechaFin = fields.Date(string='Fecha fin',required=True)
    detalles = fields.Text(string="detalles")
    idProfesor = fields.Many2one('upolang.profesor', string='Profesor')
    idEmpresa = fields.Many2one('upolang.empresa', string='Empresa')
    idAsignatura = fields.Many2many('upolang.asignatura', string='Asignatura')
    
    @api.onchange('Asignatura')
    def _onchange_asignatura(self):
        """
        Actualiza las fechas de inicio y fin del contrato según las asignaturas del profesor.
        Si hay varias asignaturas asignadas, toma la fecha de inicio más temprana
        y la fecha de fin más tardía.
        """
        if self.Asignatura:
            # Inicializar las fechas con valores extremos
            fecha_inicio = None
            fecha_fin = None

            for asignatura in self.Asignatura:
                # Obtenemos las fechas de cada asignatura
                if fecha_inicio is None or asignatura.fechaInicio < fecha_inicio:
                    fecha_inicio = asignatura.fechaInicio
                if fecha_fin is None or asignatura.fechaFin > fecha_fin:
                    fecha_fin = asignatura.fechaFin

            # Actualizar las fechas del contrato
            self.fechaInicio = fecha_inicio
            self.fechaFin = fecha_fin
    