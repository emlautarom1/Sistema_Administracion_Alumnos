from bdescuela import BDEscuela
from alumno import Alumno
from materia import Materia

# def add_user():
#     if bd_escuela.is_privileged():
#         newusername = input('Input user: ')
#         newpassword = input('Input password: ')
#         privileges = input('Input priveleges: ')
#         try:
#             bd_escuela.reg_usuario(newusername, newpassword, privileges)
#             if privilege == 'A':
#                 pass
#                 # Read new Alumno
#                 alumno = Alumno()
#                 bd_escuela.get_table('T-alumnos').alta(alumno)
#             return True
#         except KeyError:
#             print('User already in database!')
#         except ValueError:
#             print('Invalid privileges!')
#     else:
#         print('Unprivileged user')
#     return False

# def remove_user(username):
#     if bd_escuela.is_privileged():
#         try:
#             bd_escuela.elim_usuario(username)
#             return True
#         except KeyError:
#             print('User not in database!')
#     else:
#         print('Unprivileged user')
#     return False

privilege = 'P'
username = 'admin'
password = 'ad1'
save_file = '2018_ProgIII/PMP_Python/1_PracLab/pray.json'

bd_escuela = BDEscuela()
# Init database
bd_escuela.inic_esc(privilege, username, password)
# Login
al = Alumno(
    nro_reg=4000,
    nombre='Pepe',
    apellido='Test',
    dni=41140240,
    direccion='My Address',
    telefono='54654654',
    email='test@sample.com',
    nacimiento=[4, 4, 2000],
    curso=2,
    username='pythoniscool',
    password='123456'
)
# Create new Alumno
bd_escuela.reg_alumno(al)
# Register Alumno
mat = Materia('Matematica', 4000)
mat.set_notas([8.50, 4.25, 7.80])
mat2 = Materia('Lengua', 4000)
mat2.set_notas([1, 1, 1])
mat3 = Materia('Etica', 4000)
mat3.set_notas([4, 4, 4])
# Create new Materias
bd_escuela.get_table('T-materias').alta(mat)
bd_escuela.get_table('T-materias').alta(mat2)
bd_escuela.get_table('T-materias').alta(mat3)
# Add Materias
bd_escuela.backup(save_file)
# Make system backup
bd_escuela.baja_alumno(al)
# Remove alumno (also removes mat and mat2)
bd_escuela.reg_usuario('P', 'juan24', '123456789')
# Add new user
bd_escuela.carga_bd(save_file)
# Reload saved data
print('End')

# Operaciones:
#   Login: logincheck() retorna el estado de login, o un error en caso de que no se haya podiodo loguear
#   Añadir usuario: adduser() lee un usuario, contraseña y privilegios y los carga a la base de datos.
#   Eliminar usuario: removeuser() toma un useracces y lo elimina de la base de datos.
#   CRUD de Alumnos: definido en TAlumnos.
#   Listado por inasistencias: definido en TAlumnos
#   Listado ordenado por curso: definido en TAlumnos
#   Inicializacion de Sesion: definido en BDAlumnos
#   Alamcenamiento en disco: definido en BDAlumnos
