from bdescuela import BDEscuela
from alumno import Alumno
from materia import Materia
import copy

privilege = 'P'
username = 'admin'
password = 'ad1'
file_folder = '2018_ProgIII/PMP_Python/1_PracLab/'
file_name = 'database.json'
# System stress test:

# Init database
bd_escuela = BDEscuela()
# Login
bd_escuela.inic_esc(privilege, username, password)
# Add new user
bd_escuela.reg_usuario('P', 'python_admin', 'admin123')
# Create new Alumno
al = Alumno(
    nro_reg=4000,
    nombre='Python',
    apellido='Anaconda',
    dni=41140240,
    direccion='My Address',
    telefono='555-555-5555',
    email='test@sample.com',
    nacimiento=(1, 1, 2000),
    curso=3,
    username='pythoniscool',
    password='123456'
)
# Register Alumno
bd_escuela.reg_alumno(al)

# Modify Alumno
al.set_inasistencias(18)
# bd_escuela.mod_alumno(al)

# Listado_inas
inas = bd_escuela.get_table('T-alumnos').listado_inas()

# Listado_reg_x_curso
reg_x_curso = bd_escuela.get_table('T-alumnos').listado_reg_x_curso(3)

# Create new Materias
mat = Materia('Matematica', 4000)
mat.set_notas([9, 9, 9])
mat2 = Materia('Lengua', 4000)
mat2.set_notas([1, 1, 1])
mat3 = Materia('Etica', 4000)
mat3.set_notas([4, 4, 4])

# Add Materias
bd_escuela.get_table('T-materias').alta(mat)
bd_escuela.get_table('T-materias').alta(mat2)
bd_escuela.get_table('T-materias').alta(mat3)

# Materias de 4000
# materias = bd_escuela.get_table('T-materias').get_materias_de_alumno(4000)
# for m in materias:
#     print(m.get_nombre())
#     print(m.get_notas())
# print('------------')

# Make system backup
bd_escuela.backup(file_name, file_folder)

# Remove Materia
bd_escuela.get_table('T-materias').baja(4000, 'Lengua')

# Modify Materia
mat_mod = copy.copy(mat)
mat_mod.set_notas([7, 7, 7])
bd_escuela.get_table('T-materias').modificar(mat_mod)

# Remove Alumno (removes all Materias)
bd_escuela.baja_alumno(4000)

# Reload saved data
bd_escuela.carga_bd(file_name, file_folder)
print('Should be "Anaconda"')
print(bd_escuela.cons_alumno(4000).get_apellido())
print('------------')

print('Should be [9, 9, 9]:')
print(bd_escuela.get_table('T-materias').consulta(4000, 'Matematica').get_notas())
print('------------')

print('All OPs done with no errors...')
