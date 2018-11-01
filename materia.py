class Materia:

    def __init__(self, nombre, nro_reg):
        self.nombre = nombre
        self.nro_reg = nro_reg
        self.notas = [0, 0, 0]

    def get_nombre(self):
        return self.nombre

    def get_nro_reg(self):
        return self.nro_reg

    def setnota(self, trimestre: int, nota: int):
        if -1 < trimestre < 3:
            self.notas[trimestre] = nota
        else:
            raise ValueError

    def getnota(self, trimestre: int):
        if -1 < trimestre < 3:
            return self.notas[trimestre]
        else:
            raise ValueError
