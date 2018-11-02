# Sistema CRUD de Alumnos con GUI en Python 3

## Objetivo: Crear un sistema completo de administracion de alumnos y suus correspondientes materias, programadores y docentes utilizando el paradigma de POO.

### Funcionalidades

- [X] **Login**: inic_esc permite loguear al usuario al sistema, seteando el flag de privilegio en la base de datos
- [X] **Añadir usuario**: reg_usuario() permite crear un nuevo usuario a partir de un privilegio, nombre y contraseña. No se utiliza para crear alumnos.
- [ ] **Eliminar usuario**: elim_usuario() toma un nombre de usuario y un privilegio y lo elimina de la base de datos.
* **Alumnos** (definidos en bdescuela.py):
  - [X] **Alta**: reg_alumno() toma un Alumno y lo carga en la base de datos.
  - [X] **Baja**: baja_alumno() toma un numero de registro y lo elimina de la base de datos. Todas las materias asociadas al alumno son eliminadas
  - [X] **Modificacion**: mod_alumno() toma un Alumno a, busca en la base de datos un Alumno b con el mismo nro_reg y remplaza los atributos de b con los de a.
  - [X] **Consulta**: cons_alumno() toma un nro_reg y devuelve un Alumno.
  
* **Materias** (definidos en tmaterias.py):
  - [X] **Alta**: alta() toma una Materia y la carga en la base de datos.
  - [X] **Baja**: baja toma un nro_reg y un nom_materia y la elimina de la base de datos.
  - [X] **Modificacion**: modificar() toma una Materia a, busca en la base de datos una Materia b con el mismo nro_reg y el mismo nombre y remplaza los atributos de b con los de a
  - [X] **Consulta**: consulta() toma un nro_reg y un nombre y devuelve una Materia con esos valores.
  
- [X] **Listado por inasistencia** (definido en talumnos.py): devuelve una lista de Alumnos cuyas inasistencias sean mayores a 15.
- [X] **Listado ordenado por curso** (definido en talumnos.py): listado_reg_x_curso() toma un numero de curso y devuelve una lista ordenada por nombre de tuplas con datos de Alumnos que esten en el curso indicado.
* **Manejo de sesiones** (definidos en bdescuela.py):
  - [X] **Alamcenamiento en disco**: backup() toma una direccion de un archivo .json y genera una copia de todos los datos en memoria, recuperables por medio de carga_bd()
  - [X] **Inicializacion de Sesion**: carga_bd()  toma una direccion de un archivo .json y carga los datos en memoria. Si existen claves duplicadas se priorizan las que se encuentran en memoria. Se notificará al usuario en casos de que suceda.