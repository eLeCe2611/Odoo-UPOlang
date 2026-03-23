# -- coding: utf-8 --


from odoo import models, fields, api


class Asignatura(models.Model):
    _name = 'upolang.asignatura'  
    _description = 'Asignatura'

    name = fields.Char(string="Idioma", size=40,required=True)
    nivel = fields.Selection([('A1','A1'),
                              ('A2','A2'),
                              ('B1','B1'),
                              ('B2','B2'),
                              ('C1','C1'),
                              ('C2','C2')],
                              string='Nivel de la asignatura', required=True)
    descripcion = fields.Text(string="Descripción")
    fechaInicio = fields.Date(string='Fecha inicio',required=True)
    fechaFin = fields.Date(string='Fecha fin',required=True)
    duracion = fields.Integer(string="Duración (días)", compute="_compute_duracion", store=True)    
    diaSemana = fields.Selection([('lunes','lunes'),
                                  ('martes','martes'),
                                  ('miércoles','miércoles'),
                                  ('jueves','jueves'),
                                  ('viernes','viernes')],
                                  string='Dia de la semana', required=True)
    hora = fields.Selection([('08:00','08:00'),
                             ('09:00','09:00'),
                             ('10:00','10:00'),
                             ('11:00','11:00'),
                             ('12:00','12:00'),
                             ('13:00','13:00'),
                             ('14:00','14:00'),
                             ('15:00','15:00')],
                             string='Hora', required=True) # la indentación es mortal !!!
    asistentes = fields.Integer(string = "Asistentes") # debe ser calculado
    maxAsistentes = fields.Integer(string = "Maximo de asistentes")
    idAula = fields.Many2one('upolang.aula', string='Aula')    
    idTipoAsignatura = fields.Many2one('upolang.tipoasignatura', string='Tipo Asignatura')
    idContrato = fields.One2many('upolang.contrato','idAsignatura', string='Contratos')
    idEvaluacion = fields.One2many('upolang.evaluacion','idAsignatura', string='Evaluaciones')
    idValoracion = fields.One2many('upolang.valoracion','idAsignatura', string='Valoraciones')
    idCertificado = fields.Many2one('upolang.certificado', string='Certificado')    
    idProgreso = fields.Many2one('upolang.progreso', string='Progreso')    
    idMatricula = fields.One2many('upolang.matricula','idAsignatura', string='Matriculas')
    
    
    @api.onchange('Aula')
    def _onchange_idAula(self):
        """Inicializa maxAsistentes según la capacidad del aula seleccionada."""
        if self.Aula:
            self.maxAsistentes = self.Aula.capacidad

    def name_get(self):
        result = []
        for record in self:
            display_name = f"{record.name or 'Sin idioma'} - {record.nivel or 'Sin nivel'}"
            result.append((record.id, display_name))
        return result
    
    @api.depends('fechaInicio', 'fechaFin')
    def _compute_duracion(self):
        for record in self:
            if record.fechaInicio and record.fechaFin:
                start_date = fields.Date.from_string(record.fechaInicio)
                end_date = fields.Date.from_string(record.fechaFin)
                record.duracion = (end_date - start_date).days
            else:
                record.duracion = 0

    