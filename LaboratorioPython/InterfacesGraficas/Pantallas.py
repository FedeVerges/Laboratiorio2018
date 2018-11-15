from tkinter import ttk
from LaboratorioPython.Funcionalidades import *

basedatos = BD_Escuela()
basedatos.RegUs("fede","1234",2)


def cambiarPantallas(ventana, tipoVentana, tipoUsuario=-1):
    # Destruyo la ventana anterior
    ventana.frame.pack_forget()
    ventana.frame.destroy()

    # Abro una nueva ventana

    if tipoVentana == "menu principal":
        MenuPrincipal(root, tipoUsuario)
    elif tipoVentana == "agregar alumno":
        VentanaAltaAlumno(root)
    elif tipoVentana == "registrar usuario":
        VentanaUsuario(root)
    elif tipoVentana == "login":
        Login(root)


class Login:
    def __init__(self, padre):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.title('Bienvendo al Sistema de Alumnos')

        # Se definen los labels de las cajas de texto
        self.lbl_nu = ttk.Label(self.frame, text="Ingrese Nombre Usuario:")
        self.lbl_passw = ttk.Label(self.frame, text="Ingrese Contraseña:")

        self.usuario = StringVar()
        self.contraseña = StringVar()

        # se crean las cajas de entrada de texto.
        self.text_nu = ttk.Entry(self.frame, textvariable=self.usuario, width=30)
        self.passw = ttk.Entry(self.frame, textvariable=self.contraseña, width=30, show="*")

        # se definen los botones.

        self.boton_aceptar = Button(self.frame, text="Autenticar", command=self.InicEsc)
        self.boton_cancelar = Button(self.frame, text="Cancelar", command=self.frame.destroy)

        # definimos las posiciones de los componentes.
        self.lbl_nu.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.text_nu.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.lbl_passw.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.passw.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

        self.boton_aceptar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton_cancelar.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

    def InicEsc(self):
        if validarLogin(self.usuario.get(), self.contraseña.get(), basedatos) == 2:
            cambiarPantallas(self, "menu principal", 2)  # Inicia sesion Programador
        elif validarLogin(self.usuario.get(), self.contraseña.get(), basedatos) == 1:
            cambiarPantallas(self, "menu principal", 1)  # Inicia sesion Docente
        elif validarLogin(self.usuario.get(), self.contraseña.get(), basedatos) == 0:
            cambiarPantallas(self, "menu principal", 0)  # Inicia sesion Alumno
        else:
            messagebox.showerror("Usuario no existente", "El usuario o la contraseña son erroneas")
            self.passw.focus_set()


class MenuPrincipal:
    def __init__(self, padre, tipoUsuario):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.title("MENU PRINCIPAL")

        # Funcionaliddades Programador
        if tipoUsuario == 2:
            self.boton_agregar_usuario = Button(self.frame, text="Agregar Usuario",
                                                command=lambda: cambiarPantallas(self, "registrar usuario"))
            self.boton_listar_alumnos = Button(self.frame, text="Listar Alumnos", command=lambda: LisTAlu(basedatos))
            self.boton_AgregarAlumno = Button(self.frame, text="Agregar Alumnos",
                                              command=lambda: cambiarPantallas(self, "agregar alumno"))
            self.boton_salir = Button(self.frame, text="Cerrar Sesion", command=lambda: cambiarPantallas(self,"login"))
            self.boton_tablaUsarios = Button(self.frame, text="Tabla Usuarios", command=lambda: TablaUsuarios(basedatos))
            self.boton_eliminarUsuario = Button(self.frame, text="Eliminar Usuarios")

            self.boton_eliminarUsuario.pack(side=TOP)
            self.boton_agregar_usuario.pack(side=TOP)
            self.boton_tablaUsarios.pack(side=TOP)
            self.boton_AgregarAlumno.pack(side=TOP)
            self.boton_listar_alumnos.pack(side=TOP)


class VentanaAltaAlumno:
    def __init__(self, padre):
        self.frame = Frame(padre)
        padre.title("Alta Alumno")
        self.frame.pack()

        # variables
        self.nroregistro = basedatos.getCantidadAlumnos() + 1
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.telefono = IntVar()
        self.fechaNacimiento = StringVar()
        self.email = StringVar()
        self.año = IntVar()
        self.fechaAlta = StringVar()
        self.fechaBaja = StringVar()
        self.usuario = StringVar()
        self.contraseña = StringVar()
        self.inasistencias = IntVar()
        self.concepto = StringVar()

        # Creamos las etiquetas

        self.label_nombre = Label(self.frame, text="Nombre:")
        self.label_apellido = Label(self.frame, text="Apellido:")
        self.label_dni = Label(self.frame, text="DNI:")
        self.label_telefono = Label(self.frame, text="Telefono:")
        self.label_fecha = Label(self.frame, text="Fecha de Nacimiento:")
        self.label_email = Label(self.frame, text="Email:")
        self.label_año = Label(self.frame, text="Año:")
        self.label_a_fecha = Label(self.frame, text="Fecha de Alta:")
        self.label_usuario = Label(self.frame, text="Usuario:")
        self.label_concepto = Label(self.frame, text="Concepto:")
        self.label_inasistencias = Label(self.frame, text="Inasistencias:")

        # Creacion de los campos de texto

        self.texto_nombre = Entry(self.frame, textvariable=self.nombre, width=30)
        self.texto_apellido = Entry(self.frame, textvariable=self.apellido, width=30)
        self.texto_dni = Entry(self.frame, textvariable=self.dni, width=30)
        self.texto_telefono = Entry(self.frame, textvariable=self.telefono, width=30)
        self.texto_fecha = Entry(self.frame, textvariable=self.fechaNacimiento, width=30)
        self.texto_email = Entry(self.frame, textvariable=self.email, width=30)
        self.texto_año = Entry(self.frame, textvariable=self.año, width=30)
        self.texto_a_fecha = Entry(self.frame, textvariable=self.fechaAlta, width=30)
        self.texto_usuario = Entry(self.frame, textvariable=self.usuario, width=30)
        self.texto_concepto = Entry(self.frame, textvariable=self.concepto, width=30)
        self.texto_inasistencias = Entry(self.frame, textvariable=self.inasistencias, width=30)

        # Creacion de botones

        self.boton_aceptar = Button(self.frame, text="Aceptar",
                                    command=lambda: AAlumno(basedatos, self.nroregistro, self.nombre.get(),
                                                            self.apellido.get(), self.dni.get(), self.telefono.get()
                                                            , self.fechaNacimiento.get(), self.email.get(),
                                                            self.año.get(), self.fechaAlta.get(), self.fechaBaja.get()
                                                            , self.usuario.get(), self.inasistencias.get(),
                                                            self.concepto.get()))
        self.boton_modificar = Button(self.frame, text="Modificar", command=lambda: print(self.nombre.get()))
        self.boton_elimiar = Button(self.frame, text="eliminar")
        self.boton_back = Button(self.frame, text="Atras", command=lambda: cambiarPantallas(self, "menu principal",2))

        self.label_nombre.pack(side=TOP)
        self.texto_nombre.pack(side=TOP)

        self.label_apellido.pack(side=TOP)
        self.texto_apellido.pack(side=TOP)

        self.label_dni.pack(side=TOP)
        self.texto_dni.pack(side=TOP)

        self.label_telefono.pack(side=TOP)
        self.texto_telefono.pack(side=TOP)

        self.label_fecha.pack(side=TOP)
        self.texto_fecha.pack(side=TOP)

        self.label_email.pack(side=TOP)
        self.texto_email.pack(side=TOP)

        self.label_año.pack(side=TOP)
        self.texto_año.pack(side=TOP)

        self.label_a_fecha.pack(side=TOP)
        self.texto_a_fecha.pack(side=TOP)

        self.label_usuario.pack(side=TOP)
        self.texto_usuario.pack(side=TOP)

        self.label_concepto.pack(side=TOP)
        self.texto_concepto.pack(side=TOP)

        self.label_inasistencias.pack(side=TOP)
        self.texto_inasistencias.pack(side=TOP)

        self.boton_aceptar.pack(side=LEFT)
        self.boton_modificar.pack(side=LEFT)
        self.boton_back.pack(side=RIGHT)
        self.boton_elimiar.pack(side=RIGHT)


class VentanaUsuario:
    def __init__(self, padre):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.title('Registrar Usuario')

        # Se definen los labels de las cajas de texto
        self.label_nombre_usuario = Label(self.frame, text="Ingrese Nombre Usuario:")
        self.label_passw1 = Label(self.frame, text="Ingrese Contraseña:")
        self.label_passw2 = Label(self.frame, text="Ingrese Contraseña Nuevamente:")


        self.usuario = StringVar()
        self.contraseña = StringVar()
        self.contraseña2 = StringVar()
        self.opcion = IntVar()
        # se crean las cajas de entrada de texto.
        self.texto_nombre = Entry(self.frame, textvariable=self.usuario, width=30)
        self.texto_passw1 = Entry(self.frame, textvariable=self.contraseña, width=30, show="*")
        self.texto_passw2 = Entry(self.frame, textvariable=self.contraseña2, width=30, show="*")

        # Botones para tipo de usuario
        self.r_admin = Radiobutton(self.frame, text="Administrador", variable=self.opcion, value=2)
        self.r_doc = Radiobutton(self.frame, text="Docente", variable=self.opcion, value=1)

        # se definen los botones.

        self.boton_registrar = Button(self.frame, text="Registrar",
                                      command=(lambda :basedatos.RegUs(self.usuario.get(), self.contraseña.get(), self.opcion.get())))
        self.boton_cancelar = Button(self.frame, text="Cancelar", command=(lambda: cambiarPantallas(self,"menu principal",2)))
        self.boton_eliminarUsuario = Button(self.frame, text="Eliminar Usuarios", command=(lambda:basedatos.ElimUs(self.usuario.get(),)))

        # definimos las posiciones de los componentes.
        self.label_nombre_usuario.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.texto_nombre.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.label_passw1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.texto_passw1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.label_passw2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.texto_passw2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.r_admin.pack(side=LEFT)
        self.r_doc.pack(side=LEFT)


        self.boton_registrar.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton_cancelar.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
'''class ventanaEliminarUsuarios:
    def __init__(self,padre):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.title('Eliminar Usuario')

'''
root = Tk()
Login(root)
root.mainloop()
