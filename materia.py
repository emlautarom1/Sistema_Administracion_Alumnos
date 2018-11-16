class Materia:

    def __init__(self, nombre='none', nro_reg=0):
        self.__nombre = nombre
        self.__nro_reg = nro_reg
        self.__notas = [0, 0, 0]

    def get_nombre(self):
        return self.__nombre

    def get_nro_reg(self):
        return self.__nro_reg

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas: list):
        self.__notas = notas

    def set_nota_trimestre(self, trimestre: int, nota: int):
        if -1 < trimestre < 3:
            self.__notas[trimestre] = nota
        else:
            raise ValueError

    def get_nota_trimestre(self, trimestre: int):
        if -1 < trimestre < 3:
            return self.__notas[trimestre]
        else:
            raise ValueError
