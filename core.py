from tkinter import Tk, Frame, Label, Entry, Button, messagebox, ttk, StringVar
from bdescuela import BDEscuela
from alumno import Alumno
from materia import Materia

# Snippets
# messagebox.showerror("Title", "a Tk MessageBox")

def set_grid_margin(frame, col_count, row_count, sz=10):
    frame.rowconfigure(row_count+1, minsize=sz)
    frame.rowconfigure(0, minsize=sz)
    frame.columnconfigure(col_count+1, minsize=sz)
    frame.columnconfigure(0, minsize=sz)


def center(n):
    # Center window
    n.eval('tk::PlaceWindow %s center' % n.winfo_pathname(n.winfo_id()))


def swap_view(old_view, new_view):
    old_view.frame.pack_forget()
    old_view.frame.destroy()

    if new_view == 'main_menu':
        MainMenu(root)
    elif new_view == 'login':
        Login(root)
    elif new_view == 'registrar_usuario':
        RegistrarUsuario(root)
    elif new_view == 'eliminar_usuario':
        EliminarUsuario(root)
    elif new_view == 'tabla_alumno':
        raise NotImplementedError
    elif new_view == 'legajo_dni':
        raise NotImplementedError
    elif new_view == 'listado_inas':
        raise NotImplementedError
    elif new_view == 'listado_curso':
        raise NotImplementedError
    elif new_view == 'consulta_alumno':
        ConsultaAlumno(root)
    elif new_view == 'alta_alumno':
        AltaAlumno(root)
    elif new_view == 'baja_alumno':
        BajaAlumno(root)
    elif new_view == 'modificar_alumno':
        ModificarAlumno(root)
    elif new_view == 'tabla_materia':
        raise NotImplementedError
    elif new_view == 'consulta_materia':
        ConsultaMateria(root)
    elif new_view == 'alta_materia':
        AltaMateria(root)
    elif new_view == 'baja_materia':
        BajaMateria(root)
    elif new_view == 'modificar_materia':
        ModificarMateria(root)
    elif new_view == 'backup':
        Backup(root)
    elif new_view == 'restore':
        Restore(root)
    else:
        raise RuntimeError

# Layout done
class Login:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Login')
        # Widgets
        self.username_label = Label(self.frame, text='Usuario:')
        self.username_entry = Entry(self.frame)
        self.privilege_label = Label(self.frame, text='Privielgios:')
        self.privilege_combo = ttk.Combobox(self.frame, state='readonly')
        self.privilege_combo['values'] = ['Programador', 'Docente', 'Alumno']
        self.password_label = Label(self.frame, text='Contraseña:')
        self.password_entry = Entry(self.frame, show='*')
        self.login_button = Button(
            self.frame, text='Iniciar Sesión', foreground='blue', command=self.login)
        self.exit_button = Button(
            self.frame, text='Salir', foreground='red', command=exit)

        # Layout
        self.username_label.grid(row=1, column=1, sticky='E')
        self.username_entry.grid(row=1, column=2, sticky='EW')
        self.privilege_label.grid(row=2, column=1, sticky='E')
        self.privilege_combo.grid(row=2, column=2, sticky='EW')
        self.password_label.grid(row=3, column=1, sticky='E')
        self.password_entry.grid(row=3, column=2, sticky='EW')

        self.frame.rowconfigure(4, minsize=50)

        self.exit_button.grid(row=5, column=1, sticky='EW')
        self.login_button.grid(row=5, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 5, 50)

        # Center
        center(master)

    def login(self):
        # print(self.password_entry.get())
        print('Loged in...')
        swap_view(self, 'main_menu')

# Layout done
class MainMenu:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Menú Principal')
        
        # Frames
        self.system_frame = Frame(self.frame, relief='ridge', bd=5)
        self.alumno_frame = Frame(self.frame, relief='ridge', bd=5)
        self.materia_frame = Frame(self.frame, relief='ridge', bd=5)

        # Widgets

        # Usuarios
        self.usuarios_label = Label(self.system_frame, text='Usuarios')
        self.registrar_button = Button(
            self.system_frame, text='Registrar un Usuario', command=lambda: swap_view(self, 'registrar_usuario'))
        self.eliminar_button = Button(
            self.system_frame, text='Eliminar un Usuario', command=lambda: swap_view(self, 'eliminar_usuario')
        )
        # Alumnos
        self.alumno_label = Label(self.alumno_frame, text='Alumnos')
        self.tabla_alumno_button = Button(
            self.alumno_frame, text='Tabla de Alumnos', command=lambda: swap_view(self, 'tabla_alumno'))
        self.legajo_alumno_dni_button = Button(
            self.alumno_frame, text='Buscar legajo por DNI', command=lambda: swap_view(self, 'legajo_dni'))
        self.listado_inasistencias_button = Button(
            self.alumno_frame, text='Listado por Inasistencias', command=lambda: swap_view(self, 'listado_inas'))
        self.listado_curso_button = Button(
            self.alumno_frame, text='Listado por Curso', command=lambda: swap_view(self, 'listado_curso'))
        self.alumno_crud_label = Label(
            self.alumno_frame, text='Operaciones CRUD: Alumnos')
        self.consulta_alumno_button = Button(
            self.alumno_frame, text='Consultar', command=lambda: swap_view(self, 'consulta_alumno'))
        self.alta_alumno_button = Button(
            self.alumno_frame, text='Alta', command=lambda: swap_view(self, 'alta_alumno'))
        self.baja_alumno_button = Button(
            self.alumno_frame, text='Baja', command=lambda: swap_view(self, 'baja_alumno'))
        self.modificacion_alumno_button = Button(
            self.alumno_frame, text='Modificar', command=lambda: swap_view(self, 'modificar_alumno'))

        # Materias
        self.materia_label = Label(self.materia_frame, text='Materias')
        self.tabla_materia_button = Button(
            self.materia_frame, text='Tabla de Materias', command=lambda: swap_view(self, 'tabla_materia'))
        self.materia_crud_label = Label(
            self.materia_frame, text='Operaciones CRUD: Materias')
        self.consulta_materia_button = Button(
            self.materia_frame, text='Consultar', command=lambda: swap_view(self, 'consulta_materia'))
        self.alta_materia_button = Button(
            self.materia_frame, text='Alta', command=lambda: swap_view(self, 'alta_materia'))
        self.baja_materia_button = Button(
            self.materia_frame, text='Baja', command=lambda: swap_view(self, 'baja_materia'))
        self.modificacion_materia_button = Button(
            self.materia_frame, text='Modificar', command=lambda: swap_view(self, 'modificar_materia'))

        # Sesiones
        self.sesion_label = Label(self.system_frame, text='Sesiones')
        self.backup_button = Button(
            self.system_frame, text='Almacenar en Disco', command=lambda: swap_view(self, 'backup'))
        self.restore_button = Button(
            self.system_frame, text='Inicializar Sesion', command=lambda: swap_view(self, 'restore'))

        # Layout in Frames:

        # System
        self.usuarios_label.grid(row=1, sticky='EW')
        self.frame.rowconfigure(2, minsize=10)
        self.registrar_button.grid(row=3, sticky='EW')
        self.eliminar_button.grid(row=4, sticky='EW')

        self.system_frame.rowconfigure(5, minsize=20)

        self.sesion_label.grid(row=6, sticky='EW')
        self.backup_button.grid(row=7, sticky='EW')
        self.restore_button.grid(row=8, sticky='EW')
        
        # Alumnos
        self.alumno_label.grid(row=1, sticky='EW')
        self.tabla_alumno_button.grid(row=2, sticky='EW')
        self.legajo_alumno_dni_button.grid(row=3, sticky='EW')
        self.listado_inasistencias_button.grid(row=4, sticky='EW')
        self.listado_curso_button.grid(row=5, sticky='EW')
        
        self.alumno_frame.rowconfigure(6, minsize=20)
        
        self.alumno_crud_label.grid(row=7, sticky='EW')
        self.consulta_alumno_button.grid(row=8, sticky='EW')
        self.alta_alumno_button.grid(row=9, sticky='EW')
        self.baja_alumno_button.grid(row=10, sticky='EW')
        self.modificacion_alumno_button.grid(row=11, sticky='EW')

        # Materias
        self.materia_label.grid(row=1, sticky='EW')
        self.tabla_materia_button.grid(row=2, sticky='EW')
        self.materia_frame.rowconfigure(3, minsize=20)
        self.materia_crud_label.grid(row=4, sticky='EW')
        self.consulta_materia_button.grid(row=5, sticky='EW')
        self.alta_materia_button.grid(row=6, sticky='EW')
        self.baja_materia_button.grid(row=7, sticky='EW')
        self.modificacion_materia_button.grid(row=8, sticky='EW')

        # Frame layout
        self.system_frame.pack(side='left', padx=10, pady=10, fill='y')        
        self.alumno_frame.pack(side='left', padx=10, pady=10, fill='y')
        self.materia_frame.pack(side='left', padx=10, pady=10, fill='y')


        center(master)

# Layout done
class RegistrarUsuario:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Registrar Usuario')

        # Widgets
        self.privilege_label = Label(self.frame, text='Privilegio:')
        self.privilege_combo = ttk.Combobox(self.frame, state='readonly')
        self.privilege_combo['values'] = ['Programador', 'Docente']
        self.username_label = Label(self.frame, text='Usuario:')
        self.username_entry = Entry(self.frame)
        self.create_button = Button(
            self.frame, text='Registrar', foreground='green', command=self.register)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.username_label.grid(row=1, column=1)
        self.username_entry.grid(row=1, column=2, sticky='EW')
        self.privilege_label.grid(row=2, column=1)
        self.privilege_combo.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=50)

        self.return_button.grid(row=4, column=1, sticky='EW')
        self.create_button.grid(row=4, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 4)

        center(master)

    def register(self):
        print('Registrando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class EliminarUsuario:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Eliminar Usuario')

        # Widgets
        self.privilege_label = Label(self.frame, text='Privilegio:')
        self.privilege_combo = ttk.Combobox(self.frame, state='readonly')
        self.privilege_combo['values'] = ['Programador', 'Docente']
        self.username_label = Label(self.frame, text='Usuario:')
        self.username_entry = Entry(self.frame)
        self.delete_button = Button(
            self.frame, text='Eliminar', foreground='red', command=self.delete)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='green', command=self.cancel)

        # Layout
        self.username_label.grid(row=1, column=1)
        self.username_entry.grid(row=1, column=2, sticky='EW')
        self.privilege_label.grid(row=2, column=1)
        self.privilege_combo.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=50)

        self.return_button.grid(row=4, column=1, sticky='EW')
        self.delete_button.grid(row=4, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 4)

        center(master)

    def delete(self):
        print('Eliminando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class ConsultaAlumno:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        master.title('Modificar')

        # Data
        self.data = {
            'nro_reg': StringVar(),
            'nombre': StringVar(),
            'apellido': StringVar(),
            'dni': StringVar(),
            'direccion': StringVar(),
            'telefono': StringVar(),
            'email': StringVar(),
            'nacimiento': StringVar(),
            'curso': StringVar(),
            'alta': StringVar(),
            'baja': StringVar(),
            'username': StringVar(),
            'inasistencias': StringVar(),
            'concepto': StringVar()
        }

        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        
        self.search_button = Button(
            self.frame, text='Buscar', foreground='green', command=self.search)
        
        self.nombre_label = Label(self.frame, text='Nombre:')
        self.nombre_data = Entry(self.frame, textvariable=self.data['nombre'])
        self.apellido_label = Label(self.frame, text='Apellido:')
        self.apellido_data = Entry(self.frame)
        self.dni_label = Label(self.frame, text='DNI:')
        self.dni_data = Entry(self.frame)
        self.direccion_label = Label(self.frame, text='Dirección:')
        self.direccion_data = Entry(self.frame)
        self.telefono_label = Label(self.frame, text='Teléfono:')
        self.telefono_data = Entry(self.frame)
        self.email_label = Label(self.frame, text='Email')
        self.email_data = Entry(self.frame)
        self.nacimiento_label = Label(self.frame, text='Fecha Nacimiento:')
        self.nacimiento_data = Entry(self.frame)
        self.curso_label = Label(self.frame, text='Curso:')
        self.curso_data = Entry(self.frame)
        self.inasistencias_label = Label(self.frame, text='Inasistencias:')
        self.inasistencias_data = Entry(self.frame)
        self.concepto_label = Label(self.frame, text='Concepto:')
        self.concepto_data = Entry(self.frame)
        self.alta_label = Label(self.frame, text='Fecha de Alta:')
        self.alta_data = Entry(self.frame)
        self.baja_label = Label(self.frame, text='Fecha de Baja:')
        self.baja_data = Entry(self.frame)
        self.username_label = Label(self.frame, text='Usuario:')
        self.username_data = Entry(self.frame)

        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel
        )

        # Layout
        self.nro_reg_label.grid(row=1, column=1)
        self.nro_reg_entry.grid(row=1, column=2, sticky='EW')
        self.search_button.grid(row=2, column=2, sticky='EW')

        self.frame.rowconfigure(3, minsize=10)

        self.nombre_label.grid(row=4, column=1)
        self.nombre_data.grid(row=5, column=1)
        self.apellido_label.grid(row=4, column=2)
        self.apellido_data.grid(row=5, column=2)
        self.dni_label.grid(row=6, column=1)
        self.dni_data.grid(row=7, column=1)
        self.direccion_label.grid(row=6, column=2)
        self.direccion_data.grid(row=7, column=2)
        self.telefono_label.grid(row=8, column=1)
        self.telefono_data.grid(row=9, column=1)
        self.email_label.grid(row=8, column=2)
        self.email_data.grid(row=9, column=2)
        self.nacimiento_label.grid(row=10, column=1)
        self.nacimiento_data.grid(row=11, column=1)
        self.curso_label.grid(row=10, column=2)
        self.curso_data.grid(row=11, column=2)
        self.inasistencias_label.grid(row=12, column=1)
        self.inasistencias_data.grid(row=13, column=1)
        self.concepto_label.grid(row=12, column=2)
        self.concepto_data.grid(row=13, column=2)
        self.alta_label.grid(row=14, column=1)
        self.alta_data.grid(row=15, column=1)
        self.baja_label.grid(row=14, column=2)
        self.baja_data.grid(row=15, column=2)
        self.username_label.grid(row=16, column=2)
        self.username_data.grid(row=17, column=2)

        self.frame.rowconfigure(18, minsize=50)

        self.return_button.grid(row=19, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 19)

        center(master)

    def search(self):
        print('Buscando...')
        # self.data['nombre'].set('Name')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class AltaAlumno:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        master.title('Modificar')

        # Data
        self.data = {
            'nro_reg': StringVar(),
            'nombre': StringVar(),
            'apellido': StringVar(),
            'dni': StringVar(),
            'direccion': StringVar(),
            'telefono': StringVar(),
            'email': StringVar(),
            'nacimiento': StringVar(),
            'curso': StringVar(),
            'username': StringVar(),
            'password': StringVar()
        }

        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.nombre_label = Label(self.frame, text='Nombre:')
        self.nombre_entry = Entry(self.frame, textvariable=self.data['nombre'])
        self.apellido_label = Label(self.frame, text='Apellido:')
        self.apellido_entry = Entry(self.frame)
        self.dni_label = Label(self.frame, text='DNI:')
        self.dni_entry = Entry(self.frame)
        self.direccion_label = Label(self.frame, text='Dirección:')
        self.direccion_entry = Entry(self.frame)
        self.telefono_label = Label(self.frame, text='Teléfono:')
        self.telefono_entry = Entry(self.frame)
        self.email_label = Label(self.frame, text='Email')
        self.email_entry = Entry(self.frame)
        self.nacimiento_label = Label(self.frame, text='Fecha Nacimiento:')
        self.nacimiento_entry = Entry(self.frame)
        self.curso_label = Label(self.frame, text='Curso:')
        self.curso_entry = Entry(self.frame)
        self.username_label = Label(self.frame, text='Usuario:')
        self.username_entry = Entry(self.frame)
        self.password_label = Label(self.frame, text='Contraseña:')
        self.password_entry = Entry(self.frame, show='*')

        self.alta_button = Button(
            self.frame, text='Alta', foreground='green', command=self.alta)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1)
        self.nro_reg_entry.grid(row=1, column=2, sticky='EW')

        self.frame.rowconfigure(2, minsize=10)

        self.nombre_label.grid(row=3, column=1)
        self.nombre_entry.grid(row=4, column=1)
        self.apellido_label.grid(row=3, column=2)
        self.apellido_entry.grid(row=4, column=2)
        self.dni_label.grid(row=5, column=1)
        self.dni_entry.grid(row=6, column=1)
        self.direccion_label.grid(row=5, column=2)
        self.direccion_entry.grid(row=6, column=2)
        self.telefono_label.grid(row=7, column=1)
        self.telefono_entry.grid(row=8, column=1)
        self.email_label.grid(row=7, column=2)
        self.email_entry.grid(row=8, column=2)
        self.nacimiento_label.grid(row=9, column=1)
        self.nacimiento_entry.grid(row=10, column=1)
        self.curso_label.grid(row=9, column=2)
        self.curso_entry.grid(row=10, column=2)
        self.username_label.grid(row=11, column=1)
        self.username_entry.grid(row=12, column=1)
        self.password_label.grid(row=11, column=2)
        self.password_entry.grid(row=12, column=2)

        self.frame.rowconfigure(13, minsize=50)

        self.return_button.grid(row=14, column=1, sticky='EW')
        self.alta_button.grid(row=14, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 14)

        center(master)
    
    def alta(self):
        print('Cargando alumno...')
        # self.data['nombre'].set('Name')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class ModificarAlumno:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        master.title('Modificar')

        # Data
        self.data = {
            'nro_reg': StringVar(),
            'nombre': StringVar(),
            'apellido': StringVar(),
            'dni': StringVar(),
            'direccion': StringVar(),
            'telefono': StringVar(),
            'email': StringVar(),
            'nacimiento': StringVar(),
            'curso': StringVar(),
            'inasistencias': StringVar(),
            'concepto': StringVar()
        }

        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.search_button = Button(
            self.frame, text='Buscar', foreground='green', command=self.search)
        self.update_button = Button(
            self.frame, text='Modificar', foreground='blue', command=self.modify)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)
        self.nombre_label = Label(self.frame, text='Nombre:')
        self.nombre_entry = Entry(self.frame, textvariable=self.data['nombre'])
        self.apellido_label = Label(self.frame, text='Apellido:')
        self.apellido_entry = Entry(self.frame)
        self.dni_label = Label(self.frame, text='DNI:')
        self.dni_entry = Entry(self.frame)
        self.direccion_label = Label(self.frame, text='Dirección:')
        self.direccion_entry = Entry(self.frame)
        self.telefono_label = Label(self.frame, text='Teléfono:')
        self.telefono_entry = Entry(self.frame)
        self.email_label = Label(self.frame, text='Email')
        self.email_entry = Entry(self.frame)
        self.nacimiento_label = Label(self.frame, text='Fecha Nacimiento:')
        self.nacimiento_entry = Entry(self.frame)
        self.curso_label = Label(self.frame, text='Curso:')
        self.curso_entry = Entry(self.frame)
        self.inasistencias_label = Label(self.frame, text='Inasistencias:')
        self.inasistencias_entry = Entry(self.frame)
        self.concepto_label = Label(self.frame, text='Concepto:')
        self.concepto_combo = ttk.Combobox(self.frame, state='readonly')
        self.concepto_combo['values'] = [
            'Muy Aceptable', 'Aceptable', 'No aceptable']

        # Layout
        self.nro_reg_label.grid(row=1, column=1)
        self.nro_reg_entry.grid(row=1, column=2, sticky='EW')
        self.search_button.grid(row=2, column=2, sticky='EW')

        self.frame.rowconfigure(3, minsize=10)

        self.nombre_label.grid(row=4, column=1)
        self.nombre_entry.grid(row=5, column=1)
        self.apellido_label.grid(row=4, column=2)
        self.apellido_entry.grid(row=5, column=2)
        self.dni_label.grid(row=6, column=1)
        self.dni_entry.grid(row=7, column=1)
        self.direccion_label.grid(row=6, column=2)
        self.direccion_entry.grid(row=7, column=2)
        self.telefono_label.grid(row=8, column=1)
        self.telefono_entry.grid(row=9, column=1)
        self.email_label.grid(row=8, column=2)
        self.email_entry.grid(row=9, column=2)
        self.nacimiento_label.grid(row=10, column=1)
        self.nacimiento_entry.grid(row=11, column=1)
        self.curso_label.grid(row=10, column=2)
        self.curso_entry.grid(row=11, column=2)
        self.inasistencias_label.grid(row=12, column=1)
        self.inasistencias_entry.grid(row=13, column=1)
        self.concepto_label.grid(row=12, column=2)
        self.concepto_combo.grid(row=13, column=2)

        self.frame.rowconfigure(14, minsize=50)

        self.return_button.grid(row=15, column=1, sticky='EW')
        self.update_button.grid(row=15, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 15)

        center(master)

    def search(self):
        print('Buscando...')
        # self.data['nombre'].set('Name')

    def modify(self):
        print('Modificando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class BajaAlumno:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Baja')
        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.delete_button = Button(
            self.frame, text='Dar de Baja', foreground='red', command=self.delete)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='green', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1, sticky='W')
        self.nro_reg_entry.grid(row=1, column=2)

        self.frame.rowconfigure(2, minsize=50)

        self.return_button.grid(row=3, column=1, sticky='SEW')
        self.delete_button.grid(row=3, column=2, sticky='SEW')

        set_grid_margin(self.frame, 2, 3)

        center(master)

    def delete(self):
        print('Eliminando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout Done
class ConsultaMateria:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Consulta')
        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.nmbr_materia_label = Label(self.frame, text='Nombre de Materia:')
        self.nmbr_materia_entry = Entry(self.frame)

        self.nota1_label = Label(self.frame, text='Primer Trimestre:')
        self.nota1_data = Label(self.frame, text='---')

        self.nota2_label = Label(self.frame, text='Segundo Trimestre:')
        self.nota2_data = Label(self.frame, text='---')

        self.nota3_label = Label(self.frame, text='Tercer Trimestre:')
        self.nota3_data = Label(self.frame, text='---')

        self.search_button = Button(
            self.frame, text='Buscar', foreground='green', command=self.search)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1, sticky='W')
        self.nro_reg_entry.grid(row=1, column=2)
        self.nmbr_materia_label.grid(row=2, column=1, sticky='W')
        self.nmbr_materia_entry.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=5)

        self.nota1_label.grid(row=4, column=1, columnspan=2)
        self.nota1_data.grid(row=5, column=1, columnspan=2)
        self.nota2_label.grid(row=6, column=1, columnspan=2)
        self.nota2_data.grid(row=7, column=1, columnspan=2)
        self.nota3_label.grid(row=8, column=1, columnspan=2)
        self.nota3_data.grid(row=9, column=1, columnspan=2)

        self.frame.rowconfigure(10, minsize=50)

        self.return_button.grid(row=11, column=1, sticky='EW')
        self.search_button.grid(row=11, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 11)

        center(master)

    def search(self):
        print('Buscando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class AltaMateria:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Alta')
        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.nmbr_materia_label = Label(self.frame, text='Nombre de Materia:')
        self.nmbr_materia_entry = Entry(self.frame)

        self.nota1_label = Label(self.frame, text='Primer Trimestre:')
        self.nota1_entry = Entry(self.frame)

        self.nota2_label = Label(self.frame, text='Segundo Trimestre:')
        self.nota2_entry = Entry(self.frame)

        self.nota3_label = Label(self.frame, text='Tercer Trimestre:')
        self.nota3_entry = Entry(self.frame)

        self.alta_button = Button(
            self.frame, text='Alta', foreground='green', command=self.alta)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1, sticky='W')
        self.nro_reg_entry.grid(row=1, column=2)
        self.nmbr_materia_label.grid(row=2, column=1, sticky='W')
        self.nmbr_materia_entry.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=5)

        self.nota1_label.grid(row=4, column=1, columnspan=2)
        self.nota1_entry.grid(row=5, column=1, columnspan=2)
        self.nota2_label.grid(row=6, column=1, columnspan=2)
        self.nota2_entry.grid(row=7, column=1, columnspan=2)
        self.nota3_label.grid(row=8, column=1, columnspan=2)
        self.nota3_entry.grid(row=9, column=1, columnspan=2)

        self.frame.rowconfigure(10, minsize=50)

        self.return_button.grid(row=11, column=1, sticky='EW')
        self.alta_button.grid(row=11, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 11)

        center(master)

    def alta(self):
        print('Cargando materia...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class ModificarMateria:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Modificar')
        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.nmbr_materia_label = Label(self.frame, text='Nombre de Materia:')
        self.nmbr_materia_entry = Entry(self.frame)

        self.search_button = Button(
            self.frame, text='Buscar', foreground='green', command=self.search)

        self.nota1_label = Label(self.frame, text='Primer Trimestre:')
        self.nota1_entry = Entry(self.frame)

        self.nota2_label = Label(self.frame, text='Segundo Trimestre:')
        self.nota2_entry = Entry(self.frame)

        self.nota3_label = Label(self.frame, text='Tercer Trimestre:')
        self.nota3_entry = Entry(self.frame)

        self.modify_button = Button(
            self.frame, text='Modificar', foreground='blue',
            command=self.modify)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1, sticky='W')
        self.nro_reg_entry.grid(row=1, column=2)
        self.nmbr_materia_label.grid(row=2, column=1, sticky='W')
        self.nmbr_materia_entry.grid(row=2, column=2)
        self.search_button.grid(row=3, column=2, sticky='EW')

        self.frame.rowconfigure(4, minsize=5)

        self.nota1_label.grid(row=5, column=1, columnspan=2)
        self.nota1_entry.grid(row=6, column=1, columnspan=2)
        self.nota2_label.grid(row=7, column=1, columnspan=2)
        self.nota2_entry.grid(row=8, column=1, columnspan=2)
        self.nota3_label.grid(row=9, column=1, columnspan=2)
        self.nota3_entry.grid(row=10, column=1, columnspan=2)

        self.frame.rowconfigure(11, minsize=50)

        self.return_button.grid(row=12, column=1, sticky='EW')
        self.modify_button.grid(row=12, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 12)

        center(master)

    def search(self):
        print('Buscando materia...')

    def modify(self):
        print('Modificando materia...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout Done
class BajaMateria:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Baja')
        # Widgets
        self.nro_reg_label = Label(self.frame, text='Número de Registro:')
        self.nro_reg_entry = Entry(self.frame)
        self.nmbr_materia_label = Label(self.frame, text='Nombre de Materia:')
        self.nmbr_materia_entry = Entry(self.frame)
        self.delete_button = Button(
            self.frame, text='Dar de Baja', foreground='red', command=self.delete)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='green', command=self.cancel)

        # Layout
        self.nro_reg_label.grid(row=1, column=1, sticky='W')
        self.nro_reg_entry.grid(row=1, column=2)
        self.nmbr_materia_label.grid(row=2, column=1, sticky='W')
        self.nmbr_materia_entry.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=50)

        self.delete_button.grid(row=4, column=2, sticky='EW')
        self.return_button.grid(row=4, column=1, sticky='EW')

        set_grid_margin(self.frame, 2, 4)

        center(master)

    def delete(self):
        print('Eliminando...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class Backup:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Almacenar en Disco')
        # Widgets
        self.filename_label = Label(self.frame, text='Nombre:')
        self.filename_entry = Entry(self.frame)
        self.directory_label = Label(self.frame, text='Directorio:')
        self.directory_entry = Entry(self.frame)
        self.save_button = Button(
            self.frame, text='Guardar', command=self.save)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.filename_label.grid(row=1, column=1, sticky='W')
        self.filename_entry.grid(row=1, column=2)
        self.directory_label.grid(row=2, column=1, sticky='W')
        self.directory_entry.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=50)

        self.return_button.grid(row=4, column=1, sticky='EW')
        self.save_button.grid(row=4, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 4)
        # Center
        center(master)

    def save(self):
        print('Saving...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')

# Layout done
class Restore:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Inicializar Sesion')
        # Widgets
        self.filename_label = Label(self.frame, text='Nombre:')
        self.filename_entry = Entry(self.frame)
        self.directory_label = Label(self.frame, text='Directorio:')
        self.directory_entry = Entry(self.frame)
        self.save_button = Button(
            self.frame, text='Cargar', command=self.save)
        self.return_button = Button(
            self.frame, text='Cancelar', foreground='red', command=self.cancel)

        # Layout
        self.filename_label.grid(row=1, column=1, sticky='W')
        self.filename_entry.grid(row=1, column=2)
        self.directory_label.grid(row=2, column=1, sticky='W')
        self.directory_entry.grid(row=2, column=2)

        self.frame.rowconfigure(3, minsize=50)

        self.return_button.grid(row=4, column=1, sticky='EW')
        self.save_button.grid(row=4, column=2, sticky='EW')

        set_grid_margin(self.frame, 2, 4)
        # Center
        center(master)

    def save(self):
        print('Saving...')

    def cancel(self):
        print('Cancelando...')
        swap_view(self, 'main_menu')


# Start main window
root = Tk()
# Start Database

# Set login
Login(root)
# Start
root.mainloop()
