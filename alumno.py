import datetime


class Alumno:
    conceptos = {
        'MA': 'Muy Aceptable',
        'A': 'Aceptable',
        'NA': 'No aceptable'
    }

    def __init__(self, nro_reg, nombre, apellido, dni, direccion, telefono, email, nacimiento, cursando, username, password):
        self.nro_reg = nro_reg
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.nacimiento = nacimiento
        self.cursando = cursando
        self.alta = datetime.datetime.now()
        self.baja = None
        self.username = username
        self.password = password
        self.concepto = Alumno.conceptos['MA']
        self.inasistencias = 0
