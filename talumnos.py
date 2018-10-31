from alumno import Alumno


class TAlumnos:

    def __init__(self):
        self.listado = {}

    def alta(self, alumno: Alumno):
        if alumno.nro_reg not in self.listado:
            self.listado[alumno.nro_reg] = alumno
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

    def listadoinas(self):
        return filter(lambda alumno: alumno.inasistencias > 15, self.listado.values())

    def listadoregxcurso(self, curso: str):
        pass
