# -*- coding: utf-8 -*-
{
    'name': "upolang_app",

    'summary': "Gesti´on del módulo Upolang",

    'description': """
Gestión de alumnos, matrículas, profesores, aulas, etc.
""",

    'author': "TSI-Grupo1",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/profesor_view.xml',
        'views/empresa_view.xml',
        'views/asignatura_view.xml',
        'views/contrato_view.xml',
        'views/alumno_view.xml',
        'views/certificado_view.xml',
        'views/valoracion_view.xml',
        'views/progreso_view.xml',
        'views/matricula_view.xml',
        'views/metodopago_view.xml',
        'views/aula_view.xml',
        'views/evaluacion_view.xml',
        'views/factura_view.xml',
        'views/pago_view.xml',
        'views/tipoasignatura_view.xml',
        'views/menus.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

