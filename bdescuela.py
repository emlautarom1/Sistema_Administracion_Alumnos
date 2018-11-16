from alumno import Alumno
from materia import Materia
from talumnos import TAlumnos
from tmaterias import TMaterias
from singelton import Singleton
import json


class BDEscuela ():

    def __init__(self):
        self.cant_usuarios = 1
        self.acceso = {
            'P-admin': 'ad1'
        }
        self.privilege = 'NONE'
        self.priv_keys = ['A', 'P', 'D']
        self.nombre_tablas = {
            'T-alumnos': 0,
            'T-materias': 1
        }
        self.tablas = [TAlumnos(), TMaterias()]

    def inic_esc(self, privilege: str, username: str, password: str):
        key = privilege + '-' + username
        for user in self.acceso:
            if user == key:
                if self.acceso[user] == password:
                    self.privilege = privilege
                    # Set user privileges
                    return
                else:
                    raise ValueError('Contraseña incorrecta.')
        else:
            raise KeyError('El usuario no está registrado.')

    def elim_usuario(self, privilege: str, username: str):
        if self.is_privileged():
            key = privilege + '-' + username
            if key in self.acceso:
                self.acceso.pop(key)
                self.cant_usuarios -= 1
            else:
                raise KeyError('El usuario no está registrado.')
        else:
            raise PermissionError('Usted no puede realizar esta operación.')

    def reg_usuario(self, privilege: str, username: str, password: str):
        if self.is_privileged():
            if privilege in self.priv_keys:
                key = privilege + '-' + username
                if key in self.acceso:
                    raise KeyError('El usuario ya está registrado')
                else:
                    self.acceso[key] = password
                    self.cant_usuarios += 1
            else:
                raise ValueError('El tipo de usuario es inválido.')
        else:
            raise PermissionError('Usted no puede realizar esta operación.')

    def reg_alumno(self, alumno: Alumno):
        try:
            self.reg_usuario('A', alumno.get_username(), alumno.get_password())
        except:
            raise KeyError(
                'Ya existe un usuario con el nombre de usuario ingresado.')
        try:
            self.get_table('T-alumnos').alta(alumno)
        except:
            self.elim_usuario('A', alumno.get_username())
            # Remove just inserted username from acceso
            raise KeyError(
                'Ya existe un alumno con el número de registro ingresado.')

        # New alumno should init all materias. Alta/Baja?
        # self.get_table('T-materias').init_materia(alumno.get_nro_reg())

    def baja_alumno(self, nro_reg: int):
        username = self.get_table('T-alumnos').consulta(nro_reg).get_username()
        self.get_table('T-materias').baja_total(nro_reg)
        # Remove materias from alumno
        self.get_table('T-alumnos').baja(nro_reg)
        # Remove alumno from table
        self.elim_usuario('A', username)
        # Remove alumno from acces

    def mod_alumno(self, nro_reg: int, mods: dict):
        self.get_table('T-alumnos').modificar(nro_reg, mods)

    def cons_alumno(self, nro_reg: int):
        return self.get_table('T-alumnos').consulta(nro_reg)

    def is_privileged(self):
        return self.privilege == 'P' or self.privilege == 'D'

    def get_table(self, tablename: str):
        try:
            tablekey = self.nombre_tablas[tablename]
            return self.tablas[tablekey]
        except:
            raise ValueError('Invalid table name')

    def backup(self, name: str, folder: str):
        dumped = json.dumps(self,
                            default=lambda o: o.__dict__,
                            sort_keys=True,
                            indent=4)
        try:
            f = open(folder + name, 'w')
            f.write(dumped)
            f.close()
        except OSError:
            print('File {0} in {1} could not be opened.'.format(name, folder))

    def carga_bd(self, name: str, folder: str):

        try:
            f = open(folder + name, 'r')
            data = f.read()
            f.close()
        except OSError:
            print('File {0} in {1} could not be opened.'.format(name, folder))
            return

        backup = json.loads(data)
        for alum in backup['tablas'][0]['listado'].values():
            try:
                self.reg_alumno(Alumno(from_dict=alum))
            except KeyError:
                print('Alumno already in database, skipping...')

        self.acceso.update(backup['acceso'])
        self.cant_usuarios = len(self.acceso)

        for val in backup['tablas'][1]['listado']:
            materia = Materia()
            for key, value in val.items():
                setattr(materia, key, value)
            try:
                self.get_table('T-materias').alta(materia)
            except:
                print('Materia {0} from {1} already in database, skipping...'.format(
                    materia.nombre, materia.nro_reg))
