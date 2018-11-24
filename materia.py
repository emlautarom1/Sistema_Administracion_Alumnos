class Materia:

    def __init__(self, nombre='none', nro_reg=0):
        self.nombre = nombre
        self.nro_reg = nro_reg
        self.notas = [0, 0, 0]

    def get_nombre(self):
        return self.nombre

    def get_nro_reg(self):
        return self.nro_reg

    def get_notas(self):
        return self.notas

    def set_notas(self, notas: list):
        self.notas = notas

    def set_nota_trimestre(self, trimestre: int, nota: int):
        if -1 < trimestre < 3:
            self.notas[trimestre] = nota
        else:
            raise ValueError

    def get_nota_trimestre(self, trimestre: int):
        if -1 < trimestre < 3:
            return self.notas[trimestre]
        else:
            raise ValueError
