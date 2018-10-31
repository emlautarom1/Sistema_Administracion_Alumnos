from talumnos import TAlumnos
from tmaterias import TMaterias
from singelton import Singleton


class BDEscuela (metaclass=Singleton):
    cantUsuarios = 0
    acceso = {
        'P-admin': 'ad1'
    }
    # Claves de la forma:
    #   A-<username> : <password>
    #   P-<username> : <password>
    #   D-<username> : <password>
    nmbre_tablas = {
        'T-alumnos': 0,
        'T-materias': 1
    }
    tablas = [TAlumnos(), TMaterias()]

    def removeaccess(self, user: str):
        if user in self.acceso:
            self.acceso.pop(user)
        else:
            raise KeyError

    def addaccess(self, key, newpassword):
        if key in self.acceso:
            raise KeyError
        else:
            self.acceso[key] = newpassword

    def gettable(self, tablename: str):
        tablekey = self.nmbre_tablas[tablename]
        return self.tablas[tablekey]
