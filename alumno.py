import datetime


class Alumno:
    conceptos = {
        'MA': 'Muy Aceptable',
        'A': 'Aceptable',
        'NA': 'No aceptable'
    }

    def __init__(self, nro_reg, nombre, apellido, dni, direccion, telefono, email, nacimiento, curso, username, password):
        self.nro_reg = nro_reg
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.nacimiento = nacimiento
        self.curso = curso
        self.alta = datetime.datetime.now()
        self.baja = None
        self.login = (username, password)
        self.concepto = Alumno.conceptos['MA']
        self.inasistencias = 0

    def get_nro_reg(self):
        return self.nro_reg

    def set_nro_reg(self, nro_reg: int):
        self.nro_reg = nro_reg

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido: str):
        self.apellido = apellido

    def get_dni(self):
        return self.dni

    def set_dni(self, dni: int):
        self.dni = dni

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion: str):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono: int):
        self.telefono = telefono

    def get_email(self):
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_nacimiento(self):
        return self.nacimiento

    def set_nacimiento(self, nacimiento: datetime):
        self.nacimiento = nacimiento

    def get_cursando(self):
        return self.curso

    def set_curso(self, curso: int):
        self.curso = curso

    def get_alta(self):
        return self.alta

    def set_alta(self, alta: datetime):
        self.alta = datetime

    def get_baja(self):
        return self.baja

    def set_baja(self, baja: datetime):
        self.baja = datetime

    def get_username(self):
        return self.login[0]

    def set_username(self, username: str):
        self.login = (username, self.login[1])

    def get_concepto(self):
        return self.concepto

    def set_concepto(self, concepto: str):
        self.concepto = concepto

    def get_inasistencias(self):
        return self.inasistencias

    def update_inasistencias(self):
        self.inasistencias += self.inasistencias

    def correct_password(self, psw: str):
        return self.login[1] == psw
