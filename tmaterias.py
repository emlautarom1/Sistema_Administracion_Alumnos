from materia import Materia
from functools import reduce
from bisect import insort


class TMaterias:
    def __init__(self):
        self.listado = []
        self.key_alumnos = []
        self.key_materias = [
            'Matematica',
            'Lengua',
            'Fisica',
            'Quimica',
            'Biologia',
            'Etica',
            'Historia',
            'Geografia',
            'Computacion'
        ]

    def init_materia(self, nro_reg: str):
        if nro_reg not in self.key_alumnos:
            for key_materia in self.key_materias:
                self.listado.append(Materia(key_materia, nro_reg))
            self.key_alumnos.append(nro_reg)
        else:
            raise KeyError

    def get_materias_de_alumno(self, nro_reg: int):
        return filter(lambda m: m.get_nro_reg() == nro_reg, self.listado)

    def get_lis_curso(self, curso: int):
        mapped = map(lambda a: (a.get_curso(),  a.get_nombre(),
                                a.get_nro_reg(), a.get_apellido()))
        return reduce(lambda l, a: add_sorted_curso(l, a, curso), mapped)


def add_sorted_curso(l: list, a: tuple, curso: int):
    if a[0] == curso:
        insort(l, a)
