import datetime


class Alumno:
    conceptos = [
        'Muy aceptable',
        'Aceptable',
        'No aceptable'
    ]

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
            self.__nro_reg = nro_reg
            self.__nombre = nombre
            self.__apellido = apellido
            self.__dni = dni
            self.__direccion = direccion
            self.__telefono = telefono
            self.__email = email
            self.__nacimiento = nacimiento
            self.__curso = curso
            self.__alta = [datetime.datetime.now().day,
                           datetime.datetime.now().month,
                           datetime.datetime.now().year]
            self.__username = username
            self.__password = password
            self.__concepto = 'Muy aceptable'
            self.__inasistencias = 0

    def get_nro_reg(self):
        return self.__nro_reg

    def set_nro_reg(self, nro_reg: int):
        self.__nro_reg = nro_reg

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido: str):
        self.__apellido = apellido

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni: int):
        self.__dni = dni

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion: str):
        self.__direccion = direccion

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono: int):
        self.__telefono = telefono

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_nacimiento(self):
        return self.__nacimiento

    def set_nacimiento(self, nacimiento: list):
        self.__nacimiento = nacimiento

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso: int):
        self.__curso = curso

    def get_alta(self):
        return self.__alta

    def set_alta(self, alta: list):
        self.__alta = alta

    def get_username(self):
        return self.__username

    def set_username(self, username: str):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def get_concepto(self):
        return self.__concepto

    def set_concepto(self, concepto: str):
        self.__concepto = concepto

    def get_inasistencias(self):
        return self.__inasistencias

    def set_inasistencias(self, inasistencias: int):
        self.__inasistencias = inasistencias
