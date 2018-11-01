from talumnos import TAlumnos
from tmaterias import TMaterias
from singelton import Singleton


class BDEscuela ():

    def __init__(self):
        self.cantUsuarios = 0
        self.acceso = {
            'P-admin': 'ad1'
        }
        self.login_status = ''
        # Claves de la forma:
        #   A-<username> : <password>
        #   P-<username> : <password>
        #   D-<username> : <password>
        self.priv_keys = ['A', 'P', 'D']
        self.nmbre_tablas = {
            'T-alumnos': 0,
            'T-materias': 1
        }
        self.tablas = [TAlumnos(), TMaterias()]

    def login_check(self, username: str, password: str):
        for user in self.acceso:
            if user.__contains__(username):
                if self.acceso[user] == password:
                    self.login_status = user[0]
                    return
                else:
                    raise ValueError
        else:
            raise KeyError
            # Username not in acceso

    def is_privileged(self):
        return self.login_status == 'P' or self.login_status == 'D'

    def removeaccess(self, user: str):
        if self.is_privileged():
            if user in self.acceso:
                self.acceso.pop(user)
            else:
                raise KeyError
        else:
            raise PermissionError

    def addaccess(self, username, password, privilege, alumno=None):
        if self.is_privileged():
            if privilege in self.priv_keys:
                key = privilege + '-' + username
                if key in self.acceso:
                    raise KeyError
                else:
                    self.acceso[key] = password
                    if privilege == 'A':
                        self.gettable('T-alumnos').alta(alumno)
            else:
                raise ValueError
        else:
            raise PermissionError

    def gettable(self, tablename: str):
        tablekey = self.nmbre_tablas[tablename]
        return self.tablas[tablekey]
