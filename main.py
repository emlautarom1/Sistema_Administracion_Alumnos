from bdescuela import BDEscuela


def logincheck():
    for user in bd_escuela.acceso:
        if user.__contains__(username):
            if bd_escuela.acceso[user] == password:
                return user[0]
            return "Bad password"
    return "No username"


def adduser():
    if loginStatus == 'P' or loginStatus == 'A':
        newusername = input('Input user: ')
        newpassword = input('Input password: ')
        privileges = input('Input priveleges: ')
        key = privileges+'-'+newusername
        try:
            bd_escuela.addaccess(key, newpassword)
            return True
        except KeyError:
            print('User already in database!')
    else:
        print('Unprivileged user')
    return False


def removeuser(useraccess):
    if loginStatus == 'P' or loginStatus == 'A':
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
loginStatus = logincheck()

# Operaciones:
#   Login: logincheck() retorna el estado de login, o un error en caso de que no se haya podiodo loguear
#   Añadir usuario: adduser() lee un usuario, contraseña y privilegios y los carga a la base de datos.
#   Eliminar usuario: removeuser() toma un useracces y lo elimina de la base de datos.
#   CRUD de Alumnos: definido en TAlumnos.
#   Listado por inasistencias: definido en TAlumnos
#
#   Inicializacion de Sesion: pendiente
#   Alamcenamiento en disco: pendiente
#   Listado ordenado por curso: pendiente
