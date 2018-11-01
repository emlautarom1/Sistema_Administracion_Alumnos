from bdescuela import BDEscuela
from functools import reduce
from bisect import insort


def adduser():
    if bd_escuela.is_privileged():
        newusername = input('Input user: ')
        newpassword = input('Input password: ')
        privileges = input('Input priveleges: ')
        try:
            bd_escuela.addaccess(newusername, newpassword, privileges)
            return True
        except KeyError:
            print('User already in database!')
        except ValueError:
            print('Invalid privileges!')
    else:
        print('Unprivileged user')
    return False


def removeuser(useraccess):
    if bd_escuela.is_privileged():
        try:
            bd_escuela.removeaccess(useraccess)
            return True
        except KeyError:
            print('User not in database!')
    else:
        print('Unprivileged user')
    return False


def initsesion():
    pass


def storesesion():
    pass


bd_escuela = BDEscuela()
username = 'P-admin'
password = 'ad1'
bd_escuela.login(username, password)

# Operaciones:
#   Login: logincheck() retorna el estado de login, o un error en caso de que no se haya podiodo loguear
#   Añadir usuario: adduser() lee un usuario, contraseña y privilegios y los carga a la base de datos.
#   Eliminar usuario: removeuser() toma un useracces y lo elimina de la base de datos.
#   CRUD de Alumnos: definido en TAlumnos.
#   Listado por inasistencias: definido en TAlumnos
#   Listado ordenado por curso: definido en TAlumnos
#
#   Inicializacion de Sesion: pendiente
#   Alamcenamiento en disco: pendiente
