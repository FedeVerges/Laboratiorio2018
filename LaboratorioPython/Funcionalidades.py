
from LaboratorioPython.BD_Escuela import *
from tkinter import *
from tkinter import messagebox ,font
from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Materia import Materia


def validarLogin(nombre_u, passw, bdatos):
    control = -1
    acceso = bdatos.getAcceso()
    for i in acceso.keys():
        nombre = i[2:]
        prefijo = i[:2]
        if (nombre_u == nombre) and (prefijo == "P-"):
            if acceso[i] == passw:
                control = 2  # el usuario es PROGRAMADOR
        elif (nombre_u == nombre) and (prefijo == "D-"):
            if acceso[i] == passw:
                control = 1  # el usuario es DOCENTE
        elif (nombre_u == nombre) and (prefijo == "A-"):
            if acceso[i] == passw:
                control = 0  # el usuario es ALUMNO

        return control


def BackAlumnos(baseDatos=BD_Escuela()):
    tabla_alumno = baseDatos.getTablaAlumnos()
    listaAlumnos = tabla_alumno.getListaAlumnos()
    archivo = open("Alumnos.txt", "w")
    for a in listaAlumnos:
        archivo.write("---------------------------------- \n")
        archivo.write("Alumno n°" + str(a.getNroregistro()) + "\n")
        archivo.write("Nombre:" + str(a.getnombre()) + "\n")
        archivo.write("Apellido:" + str(a.getApellido()) + "\n")
        archivo.write("Dni:" + str(a.getDni()) + "\n")
        archivo.write("Telefono:" + str(a.getTelefono()) + "\n")
        archivo.write("Email:" + str(a.getEmail()) + "\n")
        archivo.write("Fecha de nacimiento:" + str(a.getFecha()) + "\n")
        archivo.write("Año que cursa:" + str(a.getAño()) + "\n")
        archivo.write("Fecha de ingreso a la institución:" + str(a.getFechaAlta()) + "\n")
        archivo.write("Fecha de baja:" + str(a.getFechaBaja()) + "\n")
        archivo.write("Usuario:" + str(a.getUsuario()) + "\n")
        archivo.write("Concepto:" + str(a.getConcepto()) + "\n")
        archivo.write("Inasistencias:" + str(a.getInasistencias()) + "\n")
    archivo.close()

def BackMaterias(tabla):
    listaMaterias = tabla.getListaMaterias()
    archivo = open("Materias.txt","w")

    for m in listaMaterias:
        archivo.write("---------------------------------- \n")
        archivo.write("Materia n°" + str(m.getCodigo()) + "\n")
        archivo.write("Nombre:" + str(m.getnombre()) + "\n")
        archivo.write("Nro Registro de Alumno:" + str(m.getCodigoAlumno()) + "\n")
        archivo.write("nota 1:" + str(m.getnota1()) + "\n")
        archivo.write("nota 2:" + str(m.getNota2()) + "\n")
        archivo.write("nota 3:" + str(m.getNota3()) + "\n")

    archivo.close()


def BackUpBD(bd):
    BackAlumnos(bd)

    BackMaterias(bd.getTablaMaterias())




def LisTAlu(bd=BD_Escuela()):
    t_alumnos = bd.getTablaAlumnos()

    root = Tk()
    root.title("Listado de Alumnos")
    root.geometry('1500x200')

    # Etiquetas

    label_norregistro = Label(root ,width=10, text="Nro \nRegistro")
    label_nombre = Label(root, text= "Nombre y Apellido")
    label_dni = Label(root ,width=10, text= "DNI")
    label_telefono = Label(root, text= "Telefono")
    label_fecha = Label(root ,width=10, text = "Fecha de\n Nacimiento")
    label_email = Label(root, text= "Email")
    label_año = Label(root, text= "Año")
    label_a_fecha = Label(root ,width=10, text= "Fecha de\n Alta")
    label_b_fecha = Label(root ,width=10, text="Fecha de\n Baja")
    label_usuario = Label(root, text= "Usuario")
    label_inasistencias = Label(root, text= "Inasistencias")
    label_concepto = Label(root, text= "Concepto")


    # ListBox (tablas)

    l_nroregistro = Listbox(root, width=10, height =15)
    l_nombres = Listbox(root, height=15)
    l_dni = Listbox(root, width=10 ,height =15)
    l_telefono = Listbox(root, height =15)
    l_fecha = Listbox(root ,width=10, height =15)
    l_email = Listbox(root, height =15)
    l_año = Listbox(root ,width=10, height =15)
    l_a_fecha = Listbox(root ,width=10, height =15)
    l_b_fecha = Listbox(root ,width=10, height =15)
    l_usuario = Listbox(root, height =15)
    l_inasistencias = Listbox(root, height =15)
    l_concepto = Listbox(root, height =15)

    for item in t_alumnos.getListaAlumnos():
        l_nroregistro.insert(0, item.getNroregistro())
        l_nombres.insert(0, item.getnombre() +"  " +item.getApellido())
        l_dni.insert(0, item.getDni())
        l_telefono.insert(0, item.getTelefono())
        l_fecha.insert(0, item.getFecha())
        l_email.insert(0, item.getEmail())
        l_año.insert(0, item.getAño())
        l_a_fecha.insert(0, item.getFechaAlta())
        l_b_fecha.insert(0, item.getFechaBaja())
        l_usuario.insert(0, item.getUsuario())
        l_inasistencias.insert(0, item.getInasistencias())
        l_concepto.insert(0, item.getConcepto())

    # acomodamos las etiquetas de las tablas
    label_norregistro.grid(row=0, column = 1)
    label_nombre.grid(row=0, column=2)
    label_dni.grid(row=0, column=3)
    label_telefono.grid(row=0, column=4)
    label_fecha.grid(row=0, column=5)
    label_email.grid(row=0, column=6)
    label_año.grid(row=0, column=7)
    label_a_fecha.grid(row=0, column=8)
    label_b_fecha.grid(row=0, column=9)
    label_usuario.grid(row=0, column=10)
    label_inasistencias.grid(row=0, column=11)
    label_concepto.grid(row=0, column=12)

    l_nroregistro.grid(row=1, column=1)
    l_nombres.grid(row=1, column=2)
    l_dni.grid(row=1, column=3)
    l_telefono.grid(row=1, column=4)
    l_fecha.grid(row=1, column=5)
    l_email.grid(row=1, column=6)
    l_año.grid(row=1, column=7)
    l_a_fecha.grid(row=1, column=8)
    l_b_fecha.grid(row=1, column=9)
    l_usuario.grid(row=1, column=10)
    l_inasistencias.grid(row=1, column=11)
    l_concepto.grid(row=1, column=12)
    root.mainloop()

def TablaUsuarios(bd=BD_Escuela()):
    acceso = bd.getAcceso()

    root = Tk()
    root.title("Listado de Alumnos")
    root.geometry('400x600')

    # Etiquetas

    label_usuario = Label(root, width=15, text="Usuario")
    label_contraseña = Label(root,width = 15, text="Contraseña")
    label_tipo = Label(root, width=15, text="Tipo")

    # ListBox
    l_usuario = Listbox(root, width=15, height=15)
    l_contaseña = Listbox(root,width = 15, height=15)
    l_tipo = Listbox(root, width=20, height=15)



    for item in acceso.items():
        l_usuario.insert(0, item[0][2:])
        l_contaseña.insert(0, item[1])
        if item[0][:2]=="P-":
            l_tipo.insert(0, "ADMINISTRADOR")
        elif item[0][:2]=="D-":
            l_tipo.insert(0, "DOCENTE")
        elif item[0][:2]=="A-":
            l_tipo.insert(0, "ALUMNO")

    # acomodalos los componentes
    label_usuario.grid(row=0, column = 1)
    label_contraseña.grid(row=0, column=2)
    label_tipo.grid(row=0, column=3)

    l_usuario.grid(row=1, column = 1)
    l_contaseña.grid(row=1, column = 2)
    l_tipo.grid(row=1, column = 3)

    root.mainloop()

def ListMat(base_datos=BD_Escuela()):

    root = Tk()
    root.title("Listado de Alumnos")
    root.geometry('600x600')
    tabla = T_Materias()
    tabla = base_datos.getTablaMaterias()

    # Etiquetas
    label_registro_alumno = Label(root, text="Registro")
    label_CodigoMateria = Label(root, text="Codigo de\n Materia")
    label_Materia1 = Label(root, text="Nombre de la Materia")
    label_nota1 = Label(root, text="nota 1")
    label_nota2 = Label(root, text="nota 2")
    label_nota3 = Label(root, text="nota 3")

    # listBox
    l_registro = Listbox(root, width=10, height=15)
    l_codigo_materia = Listbox(root, width=10, height=15)
    l_materia = Listbox(root, width=20, height=15)
    l_nota1= Listbox(root, width=10, height=15)
    l_nota2 = Listbox(root, width=10, height=15)
    l_nota3 = Listbox(root, width=10, height=15)

    for item in tabla.getListaMaterias():
        l_registro.insert(0, item.getCodigoAlumno())
        l_codigo_materia.insert(0, item.getCodigo())
        l_materia.insert(0, item.getnombre())
        l_nota1.insert(0, item.getnota1())
        l_nota2.insert(0, item.getNota2())
        l_nota3.insert(0, item.getNota3())


    # acomodamos

    label_registro_alumno.grid(row=0, column = 1)
    label_CodigoMateria.grid(row=0, column = 2)
    label_Materia1.grid(row=0, column = 3)
    label_nota1.grid(row=0, column = 4)
    label_nota2.grid(row=0, column = 5)
    label_nota3.grid(row=0, column = 6)

    l_registro.grid(row=1, column = 1)
    l_codigo_materia.grid(row=1, column = 2)
    l_materia.grid(row=1, column = 3)
    l_nota1.grid(row=1, column = 4)
    l_nota2.grid(row=1, column = 5)
    l_nota3.grid(row=1, column = 6)

    root.mainloop()


'''
def ventanaAltaAlumno(bdatos = BD_Escuela()):

    ventana = Tk()
    ventana.geometry("400x600")

    # variables
    nroregistro = bdatos.getCantidadAlumnos()+1
    nombre = StringVar()
    apellido = StringVar()
    dni = IntVar()
    telefono = IntVar()
    fechaNacimiento = StringVar()
    email = StringVar()
    año = IntVar()
    fechaAlta = StringVar()
    fechaBaja = StringVar()
    usuario = StringVar()
    contraseña = StringVar()
    inasistencias = IntVar()
    concepto = StringVar()

    # Creamos las etiquetas

    label_nombre = Label(ventana, text="Nombre:")
    label_apellido = Label(ventana, text="Apellido:")
    label_dni = Label(ventana, text="DNI:")
    label_telefono = Label(ventana, text="Telefono:")
    label_fecha = Label(ventana,  text="Fecha de Nacimiento:")
    label_email = Label(ventana, text="Email:")
    label_año = Label(ventana, text="Año:")
    label_a_fecha = Label(ventana, text="Fecha de Alta:")
    label_usuario = Label(ventana, text="Usuario:")
    label_concepto = Label(ventana, text="Concepto:")
    label_inasistencias = Label(ventana, text="Inasistencias:")

    # Creacion de los campos de texto

    texto_nombre = Entry(ventana, textvariable=self.nombre, width=30)
    texto_apellido = Entry(ventana, textvariable=apellido, width=30)
    texto_dni = Entry(ventana, textvariable=dni, width=30)
    texto_telefono = Entry(ventana, textvariable=telefono, width=30)
    texto_fecha= Entry(ventana, textvariable= fechaNacimiento, width=30)
    texto_email = Entry(ventana, textvariable=email, width=30)
    texto_año = Entry(ventana, textvariable=año, width=30)
    texto_a_fecha = Entry(ventana, textvariable=fechaAlta, width=30)
    texto_usuario = Entry(ventana, textvariable=usuario, width=30)
    texto_concepto = Entry(ventana, textvariable=concepto, width=30)
    texto_inasistencias = Entry(ventana, textvariable=inasistencias, width=30)

    # Creacion de botones

    # boton_aceptar = Button(ventana, text="Aceptar", command=lambda: AAlumno(bdatos,nroregistro,nombre.get(),apellido.get(),dni.get(),telefono.get(),fechaNacimiento.get(),email.get(),año.get(),fechaAlta.get(),fechaBaja.get(),usuario.get(),inasistencias.get(),concepto.get()))
    boton_modificar = Button(ventana, text="Modificar", command=lambda: print(nombre.get()))
    boton_elimiar = Button(ventana, text="eliminar")

    label_nombre.pack(side=TOP)
    texto_nombre.pack(side=TOP)

    label_apellido.pack(side=TOP)
    texto_apellido.pack(side=TOP)

    label_dni.pack(side=TOP)
    texto_dni.pack(side=TOP)

    label_telefono.pack(side=TOP)
    texto_telefono.pack(side=TOP)

    label_fecha.pack(side=TOP)
    texto_fecha.pack(side=TOP)

    label_email.pack(side=TOP)
    texto_email.pack(side=TOP)

    label_año.pack(side=TOP)
    texto_año.pack(side=TOP)

    label_a_fecha.pack(side=TOP)
    texto_a_fecha.pack(side=TOP)

    label_usuario.pack(side=TOP)
    texto_usuario.pack(side=TOP)

    label_concepto.pack(side=TOP)
    texto_concepto.pack(side=TOP)

    label_inasistencias.pack(side=TOP)
    texto_inasistencias.pack(side=TOP)


#     boton_aceptar.pack(side=LEFT)
    boton_modificar.pack(side=LEFT)
    boton_elimiar.pack(side=RIGHT)

    ventana.mainloop()
    
    '''

def AAlumno(bdatos,nroRegistro=0 ,nombre="defecto" ,apellido="" ,dni=55 ,telefono=0 ,fecha=0 ,email="" ,año=0
            ,fechaAlta=0 ,fechaBaja=0 ,usuario="" ,concepto="" ,inasistencias=0):

    a = Alumnos(nroRegistro,nombre, apellido, dni, telefono, email, fecha, año, fechaAlta, fechaBaja,usuario
                , concepto, inasistencias)
    print(a.getEmail())
    if bdatos.AltaAlumnoBaseDatos(a):
        mensaje = messagebox.showinfo("Alumno Cargado"
                                      ,"El alumno: " +a.getnombre( ) +a.getApellido( ) +" \n ha sido cargado exitosamente")
    else:
        error = messagebox.showerror("Error Registro" ,"Ya existe un alumno en la base de datos")


def CAlumno(bdatos=BD_Escuela(),nro_registro=0):
    tabla = bdatos.getTablaAlumnos()
    a = Alumnos()
    a = tabla.ConsultaAlumno(nro_registro)
    return a




