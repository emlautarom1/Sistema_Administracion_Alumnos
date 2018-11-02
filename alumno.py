import datetime


class Alumno:
    conceptos = {
        'MA': 'Muy Aceptable',
        'A': 'Aceptable',
        'NA': 'No aceptable'
    }

    def __init__(self,
                 nro_reg=0,
                 nombre='none',
                 apellido='none',
                 dni=0,
                 direccion='none',
                 telefono='none',
                 email='none',
                 nacimiento=[0, 0, 0],
                 curso=0,
                 username='none',
                 password='none',
                 from_dict={},
                 ):
        if len(from_dict) != 0:
            for key, value in from_dict.items():
                setattr(self, key, value)
        else:
            self.nro_reg = nro_reg
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni
            self.direccion = direccion
            self.telefono = telefono
            self.email = email
            self.nacimiento = nacimiento
            self.curso = curso
            self.alta = (datetime.datetime.now().day,
                         datetime.datetime.now().month,
                         datetime.datetime.now().year)
            self.baja = [0, 0, 0]
            self.username = username
            self.password = password
            self.concepto = Alumno.conceptos['MA']
            self.inasistencias = 0

    def get_nro_reg(self):
        return self.nro_reg

    def set_nro_reg(self, nro_reg: int):
        self.nro_reg = nro_reg

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

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

    def set_nacimiento(self, nacimiento: list):
        self.nacimiento = nacimiento

    def get_curso(self):
        return self.curso

    def set_curso(self, curso: int):
        self.curso = curso

    def get_alta(self):
        return self.alta

    def set_alta(self, alta: list):
        self.alta = alta

    def get_baja(self):
        return self.baja

    def set_baja(self, baja: list):
        self.baja = baja

    def get_username(self):
        if type(self.username) == tuple:
            print('FAIL')
        return self.username

    def set_username(self, username: str):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password: str):
        self.password = password

    def get_concepto(self):
        return self.concepto

    def set_concepto(self, concepto: str):
        self.concepto = concepto

    def get_inasistencias(self):
        return self.inasistencias

    def set_inasistencias(self, inasistencias: int):
        self.inasistencias = inasistencias

    def update_inasistencias(self):
        self.inasistencias += self.inasistencias

    def correct_password(self, psw: str):
        return self.password == psw
