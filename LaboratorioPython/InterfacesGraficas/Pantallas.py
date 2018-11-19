from tkinter import ttk


from LaboratorioPython.Funcionalidades import *

basedatos = BD_Escuela()
basedatos.RegUs("fede","1234",2)

a = Alumnos(0,"juan","perez",41221770,2664372050,"armando@jofre@gmail.com","16/06/1998",4,"2005","0","juan","MA",10)
a2 = Alumnos(0,"jose","Di Marco",3028516,1155664461,"j_Dmarco@mail.com","16/09,1935",1,"2003","0","jose35","NA",10)
basedatos.AltaAlumnoBaseDatos(a)
basedatos.AltaAlumnoBaseDatos(a2)




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
    elif tipoVentana=="materias":
        VentanaMaterias(root,tipoUsuario)
    elif tipoVentana=="legajo":
        Legajo(root,tipoUsuario)
    elif tipoVentana=="backup":
        pantallaArchivo(root,tipoUsuario)



class Login:
    def __init__(self, padre):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.geometry("400x300")
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
        padre.geometry("600x600")
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
            self.boton_consultar_notas= Button(self.frame,text="Consultar Notas", command=lambda: cambiarPantallas(self,"materias",tipoUsuario))
            self.boton_listado_materias = Button(self.frame, text="Listado Materias", command=lambda: ListMat(basedatos))
            self.boton_legajo = Button(self.frame,text="Legajo",command=lambda: cambiarPantallas(self,"legajo",tipoUsuario))
            self.boton_Backup = Button(self.frame, text="BackUP",
                                       command=lambda:cambiarPantallas(self,"backup",tipoUsuario))




            self.boton_agregar_usuario.pack(side=TOP)
            self.boton_tablaUsarios.pack(side=TOP)
            self.boton_AgregarAlumno.pack(side=TOP)
            self.boton_listar_alumnos.pack(side=TOP)
            self.boton_consultar_notas.pack(side=TOP)
            self.boton_listado_materias.pack(side=TOP)
            self.boton_legajo.pack(side=TOP)
            self.boton_Backup.pack(side=TOP)
            self.boton_salir.pack(side=RIGHT)


class VentanaAltaAlumno:
    def __init__(self, padre):
        self.frame = Frame(padre)
        padre.geometry("400x800")
        padre.title("Alta Alumno")
        self.frame.pack()

        # variables
        self.nroregistro = IntVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.telefono = IntVar()
        self.fechaNacimiento = StringVar()
        self.email1 = StringVar()
        self.año = IntVar()
        self.fechaAlta = StringVar()
        self.fechaBaja = StringVar()
        self.usuario = StringVar()
        self.contraseña = StringVar()
        self.inasistencias = IntVar()
        self.concepto = StringVar()

        # Creamos las etiquetas
        self.label_nro_registro = Label(self.frame, text="Registro:")
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
        self.texto_nro_registro = Entry(self.frame, textvariable=self.nroregistro, width=30)
        self.texto_nro_registro.config(state="disabled")
        self.texto_nombre = Entry(self.frame, textvariable=self.nombre, width=30)
        self.texto_apellido = Entry(self.frame, textvariable=self.apellido, width=30)
        self.texto_dni = Entry(self.frame, textvariable=self.dni, width=30)
        self.texto_telefono = Entry(self.frame, textvariable=self.telefono, width=30)
        self.texto_fecha = Entry(self.frame, textvariable=self.fechaNacimiento, width=30)
        self.texto_email = Entry(self.frame, textvariable=self.email1, width=30)
        self.texto_año = Entry(self.frame, textvariable=self.año, width=30)
        self.texto_a_fecha = Entry(self.frame, textvariable=self.fechaAlta, width=30)
        self.texto_usuario = Entry(self.frame, textvariable=self.usuario, width=30)
        self.texto_concepto = Entry(self.frame, textvariable=self.concepto, width=30)
        self.texto_inasistencias = Entry(self.frame, textvariable=self.inasistencias, width=30)

        # Creacion de botones

        self.boton_aceptar = Button(self.frame, text="Aceptar",
                                    command=lambda: AAlumno(basedatos, self.nroregistro.get(), self.nombre.get(),
                                                            self.apellido.get(), self.dni.get(), self.telefono.get()
                                                            , self.fechaNacimiento.get(), self.email1.get(),
                                                            self.año.get(), self.fechaAlta.get(), self.fechaBaja.get()
                                                            , self.usuario.get(), self.inasistencias.get(),
                                                            self.concepto.get()))
        self.boton_modificar = Button(self.frame, text="Modificar", command=lambda: MAlumno(basedatos, self.nroregistro.get(), self.nombre.get(),
                                                            self.apellido.get(), self.dni.get(), self.telefono.get()
                                                            , self.fechaNacimiento.get(), self.email1.get(),
                                                            self.año.get(), self.fechaAlta.get(), self.fechaBaja.get()
                                                            , self.usuario.get(), self.inasistencias.get(),
                                                            self.concepto.get()))

        self.boton_elimiar = Button(self.frame, text="eliminar", command=lambda: EAlumno(basedatos,self.nroregistro.get()))
        self.boton_back = Button(self.frame, text="Atras", command=lambda: cambiarPantallas(self, "menu principal",2))
        self.boton_consulta = Button(self.frame, text="Consulta", command= lambda:self.setearTexto(self.nroregistro.get()))

        self.boton_consulta.pack(side=RIGHT)

        self.label_nro_registro.pack(side=TOP)
        self.texto_nro_registro.pack(side=TOP)



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
        self.boton_elimiar.pack(side=LEFT)


    def setearTexto(self,nro_registro):

        if nro_registro==0:
            self.texto_nro_registro.config(state="normal")
        else:
            a = Alumnos()
            a = CAlumno(basedatos,nro_registro)
            if not a:
                messagebox.showinfo("Alumno no existente","No Existe ese alumno en la base de datos")
            else:
                self.nroregistro.set(a.getNroregistro())
                self.nombre.set(a.getnombre())
                self.apellido.set(a.getApellido())
                self.dni.set(a.getDni())
                self.telefono.set(a.getTelefono())
                self.email1.set(a.getEmail())
                self.fechaNacimiento.set(a.getFecha())
                self.fechaAlta.set(a.getFechaAlta())
                self.fechaBaja.set(a.getFechaBaja())
                self.usuario.set(a.getUsuario())
                self.concepto.set(a.getConcepto())
                self.inasistencias.set(a.getInasistencias())


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
        self.opcion.set(-1)

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

        self.boton_eliminarUsuario = Button(self.frame, text="Eliminar Usuarios", command=(lambda: basedatos.ElimUs(self.usuario.get())))


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
        self.boton_eliminarUsuario.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

class VentanaMaterias:
    def __init__(self,padre,tipoUsuario):
        self.frame = Frame(padre)
        self.frame.grid()
        padre.title('Materias')

        # variables
        self.registro=IntVar()
        self.codigoMateria=IntVar()
        self.nota1=IntVar()
        self.nota2 = IntVar()
        self.nota3 = IntVar()

        # Labels
        self.label_registro_alumno = Label(self.frame, text="Registro")
        self.label_nombre_alumno = Label(self.frame,text="Alumno")
        self.label_CodigoMateria = Label(self.frame, text="Codigo de Materia")
        self.label_Materia1 = Label(self.frame,text="")
        self.label_nota1 = Label(self.frame,text="nota 1")
        self.label_nota2 = Label(self.frame, text="nota 2")
        self.label_nota3 = Label(self.frame, text="nota 3")

        # Campos de texto
        self.texto_registro = Entry(self.frame, textvariable=self.registro, width=10)
        self.texto_codigoMateria = Entry(self.frame, textvariable=self.codigoMateria, width=10)
        self.texto_nota1 = Entry(self.frame, textvariable= self.nota1,width =10)
        self.texto_nota2 = Entry(self.frame, textvariable=self.nota2,width =10)
        self.texto_nota3 = Entry(self.frame, textvariable=self.nota3,width =10)

        # Botones
        self.boton_consultar = Button(self.frame,text="Consultar",width =15,command=lambda:self.setearTexto(self.registro.get(),self.codigoMateria.get()))
        self.boton_cargar = Button(self.frame, text="Cargar Notas",width =15,command=lambda: self.setNotas(self.registro.get(), self.codigoMateria.get(), self.nota1.get(), self.nota2.get(), self.nota3.get()))
        self.boton_back = Button(self.frame,text="Volver",width =15,command=lambda:cambiarPantallas(self,"menu principal",tipoUsuario))
        self.boton_eliminar = Button(self.frame, text="Reset",width =15,command =lambda : self.setNotas(self.registro.get(), self.codigoMateria.get()))

        # posiciones
        self.label_registro_alumno.grid(row=0,column =1)
        self.texto_registro.grid(row=0,column=2)
        self.label_CodigoMateria.grid(row=1,column=1)
        self.texto_codigoMateria.grid(row=1,column=2)
        self.label_nombre_alumno.grid(row=4,column=1)
        self.label_Materia1.grid(row=4,column=2)
        self.label_nota1.grid(row=7,column=1)
        self.label_nota2.grid(row=8,column=1)
        self.label_nota3.grid(row=9,column=1)
        self.texto_nota1.grid(row=7,column=2)
        self.texto_nota2.grid(row=8,column=2)
        self.texto_nota3.grid(row=9,column=2)

        self.boton_consultar.grid(row=1,column=5)
        self.boton_cargar.grid(row=10,column=1)
        self.boton_back.grid(row=10,column=5)
        self.boton_eliminar.grid(row=10,column=3)

    def setearTexto(self, nro_registro,codigo_materia):
        m = Materia()

        tabla = basedatos.getTablaMaterias()

        m = tabla.ConsultaMat(nro_registro,codigo_materia)
        self.label_Materia1.config(text=m.getnombre())

        self.nota1.set(m.getnota1())
        self.nota1.set(m.getNota2())
        self.nota1.set(m.getNota3())

    def setNotas(self,nro_registro,codigo,nota1=0,nota2=0,nota3=0):

        tabla = basedatos.getTablaMaterias()
        m = tabla.ConsultaMat(nro_registro, codigo)
        m.setNota1(nota1)
        m.setNota2(nota2)
        m.setNota3(nota3)
        tabla.ModificacionMat(m)
        basedatos.setTablaMaterias(tabla)

class Legajo:
    def __init__(self,padre,tipoUsuario):
        self.frame = Frame(padre)
        self.frame.grid()
        padre.title('Legajo')

        # variables
        self.dni = IntVar()

        # label

        self.label_dni = Label(self.frame,text="Ingrese el dni")
        self.label_registro_alumno = Label(self.frame, text="Legajo")
        self.label_Materia1 = Label(self.frame, text="Nombre de la Materia")
        self.label_nota1 = Label(self.frame, text="nota 1")
        self.label_nota2 = Label(self.frame, text="nota 2")
        self.label_nota3 = Label(self.frame, text="nota 3")

        # texto

        self.t_dni = Entry(self.frame, textvariable= self.dni,width =10)

        # boton
        self.boton_legajo= Button(self.frame,text="Buscar Legajo",command=lambda :self.LisLegA(self.dni.get()))
        self.boton_back = Button(self.frame, text="Volver",command=lambda:cambiarPantallas(self,"menu principal",tipoUsuario))
        # listBox

        self.l_alumno = Listbox(self.frame, width=20, height=15)
        self.l_materias = Listbox(self.frame, width=20, height=15)
        self.l_nota1 = Listbox(self.frame, width=10, height=15)
        self.l_nota2 = Listbox(self.frame, width=10, height=15)
        self.l_nota3 = Listbox(self.frame, width=10, height=15)

        self.label_dni.grid(row=0,column=1)
        self.t_dni.grid(row=0, column=2)

        self.label_registro_alumno.grid(row=1,column=1)
        self.label_Materia1.grid(row=1, column=2)
        self.label_nota1.grid(row=1, column=3)
        self.label_nota2.grid(row=1, column=4)
        self.label_nota3.grid(row=1, column=5)

        self.boton_legajo.grid(row=0,column=3)
        self.boton_back.grid(row=3,column=6)

        self.l_alumno.grid(row=2,column=1)
        self.l_materias.grid(row=2,column=2)
        self.l_nota1.grid(row=2,column=3)
        self.l_nota2.grid(row=2,column=4)
        self.l_nota3.grid(row=2,column=5)




    def LisLegA(self,dni):

            self.tabla = basedatos.getTablaAlumnos()
            print(dni)

            self.a = self.tabla.legajo(dni)

            print(self.a)

            # Listbox alumno


            self.l_alumno.insert(0, self.a.getNroregistro())
            self.l_alumno.insert(1, self.a.getnombre() + self.a.getApellido())
            self.l_alumno.insert(2, self.a.getDni())
            self.l_alumno.insert(3, self.a.getTelefono())
            self.l_alumno.insert(4, self.a.getFecha())
            self.l_alumno.insert(5, self.a.getEmail())
            self.l_alumno.insert(6, self.a.getAño())
            self.l_alumno.insert(7, self.a.getFechaAlta())
            self.l_alumno.insert(8, self.a.getFechaBaja())
            self.l_alumno.insert(9, self.a.getUsuario())
            self.l_alumno.insert(10, self.a.getInasistencias())
            self.l_alumno.insert(11, self.a.getConcepto())

            self.tabla= basedatos.getTablaMaterias()
            self.lista = self.tabla.ConsultLegajo(self.a.getNroregistro())


            for i in self.lista:
                self.l_materias.insert(0, i.getnombre())
                self.l_nota1.insert(0, i.getnota1())
                self.l_nota2.insert(0, i.getNota2())
                self.l_nota3.insert(0, i.getNota3())



# def cargarBD(archivoAlumno,ArchivoMateria):

class pantallaArchivo:
    def __init__(self,padre,tipoUsuario):
        self.frame = Frame(padre)
        self.frame.pack()
        padre.geometry("400x200")
        padre.title('BackUp')

        # Variables
        self.archivo = StringVar()

        #Label
        self.label_nombre_archivo = Label(self.frame, text="Archivo")

        #Texto
        self.texto_archivo = Entry(self.frame, textvariable=self.archivo)

        # Boton
        self.boton_backup = Button(self.frame,text="Hacer BackUp",command=lambda:BackUpBD(basedatos,self.archivo.get()))
        self.boton_back = Button(self.frame, text="Volver",command=lambda:cambiarPantallas(self,"menu principal",tipoUsuario))

        #Posiciones
        self.label_nombre_archivo.pack(side=LEFT)
        self.texto_archivo.pack(side=LEFT)
        self.boton_backup.pack(side=LEFT)
        self.boton_back.pack(side=BOTTOM)






root = Tk()
Login(root)
root.mainloop()
