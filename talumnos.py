from alumno import Alumno
from functools import reduce


def aux(l: list, a: tuple, c: int):
    if a[0] == c:
        if len(l) == 0:
            l.append(a)
        else:
            for i, val in enumerate(l):
                if a[1] < val[1]:
                    l.insert(i, a)
                    break
            else:
                l.append(a)
    return l


class TAlumnos:

    def __init__(self):
        self.listado = {}

    def alta(self, alumno: Alumno):
        if alumno.get_nro_reg() not in self.listado:
            self.listado[alumno.get_nro_reg()] = alumno
        else:
            raise KeyError

    def baja(self, nro_reg: int):
        if nro_reg in self.listado:
            self.listado.pop(nro_reg)
        else:
            raise KeyError

    def consulta(self, nro_reg: int):
        if nro_reg in self.listado:
            return self.listado[nro_reg]
        else:
            raise KeyError

    def listado_inas(self):
        # Returns list of Alumnos
        return filter(lambda alumno: alumno.inasistencias > 15, self.listado.values())

    def listado_reg_x_curso(self, curso: str):
        mapped = map(lambda a:
                     (
                         a.get_curso(),
                         a.get_apellido(),
                         a.get_nombre(),
                         a.get_nro_reg()
                     ),
                     self.listado)
        return reduce(lambda acc, x: aux(acc, x, curso), mapped, [])
