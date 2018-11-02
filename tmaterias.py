from materia import Materia
from functools import reduce
from bisect import insort


class TMaterias:
    def __init__(self):
        self.listado = []
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

    #
    # REMOVE KEY_ALUMNOS
    #

    def alta(self, mat: Materia):
        for val in self.listado:
            if mat.get_nombre() == val.get_nombre() and mat.get_nro_reg() == val.get_nro_reg():
                raise KeyError('Materia already in database')
        self.listado.append(mat)

    def baja(self, nro_reg: int, nom_mat: str):
        for val in self.listado:
            if nro_reg == val.get_nro_reg() and nom_mat == val.get_nombre():
                self.listado.remove(val)
                break
        else:
            raise KeyError('Materia not in database')

    def baja_total(self, nro_reg: int):
        to_remove = []
        for val in self.listado:
            if val.get_nro_reg() == nro_reg:
                to_remove.append(val)
        if len(to_remove) == 0:
            raise KeyError('No materias with designated nro_reg')
        for val in to_remove:
            self.listado.remove(val)

    def consulta(self, nro_reg: int, nom_mat: str):
        for val in self.listado:
            if nro_reg == val.get_nro_reg()and nom_mat == val.get_nombre():
                return val
        else:
            raise KeyError('Materia not in database')

    def init_materia(self, nro_reg: str):
        for key_materia in self.key_materias:
            self.alta(Materia(key_materia, nro_reg))

    def get_materias_de_alumno(self, nro_reg: int):
        return filter(lambda m: m.get_nro_reg() == nro_reg, self.listado)

    def get_lis_curso(self, curso: int):
        mapped = map(lambda a: (a.get_curso(),  a.get_nombre(),
                                a.get_nro_reg(), a.get_apellido()))
        return reduce(lambda l, a: add_sorted_curso(l, a, curso), mapped)


def add_sorted_curso(l: list, a: tuple, curso: int):
    if a[0] == curso:
        insort(l, a)
