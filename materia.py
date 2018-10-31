class Materia:

    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = [0, 0, 0]

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
