import functools

from LaboratorioPython.BD_Escuela import *
from tkinter import *
from tkinter import messagebox, font
from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Materia import Materia


def validarLogin(nombre_u, passw, bdatos):
    control = -1
    acceso = bdatos.getAcceso()
    for i in acceso.items():
        nombre = i[0][2:]
        prefijo = i[0][:2]

        if (nombre_u == nombre) and (prefijo == "P-"):
            if i[1] == passw:
                control = 2  # el usuario es PROGRAMADOR
        elif (nombre_u == nombre) and (prefijo == "D-"):
            if i[1] == passw:
                control = 1  # el usuario es DOCENTE
        elif (nombre_u == nombre) and (prefijo == "A-"):
            if i[1] == passw:
                control = 0  # el usuario es ALUMNO

    return control


def BackUpBD(bd=BD_Escuela(), nombreArchivo=""):
    tabla_alumno = bd.getTablaAlumnos()
    tabla_materias = bd.getTablaMaterias()
    listaAlumnos = tabla_alumno.getListaAlumnos()
    listaMaterias = tabla_materias.getListaMaterias()
    archivo = open(nombreArchivo, "w")

    # BackUp datos Base de datos.

    archivo.write("Cantidad de Usuarios:" + str(bd.getCantidadusuarios()) + "\n")
    archivo.write("Acceso:")
    for i in bd.getAcceso().items():
        archivo.write(str(i[0]) + "," + str(i[1]) + " ")
    archivo.write("\nNombre de las tablas:")
    for i in bd.getNombreTablas().items():
        archivo.write(i[0] + "," + str(i[1]) + " ")

    archivo.write("\n\n")
    # BackUp de Alumnos

    for a in listaAlumnos:
        archivo.write("----" + "\n")
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
        archivo.write("Inasistencias:" + str(a.getInasistencias()) + " \n")

    # BackUp de Materias

    archivo.write("\n")
    for m in listaMaterias:
        archivo.write("----\n")
        archivo.write("Materia n°" + str(m.getCodigo()) + "\n")
        archivo.write("Nombre:" + str(m.getnombre()) + "\n")
        archivo.write("Nro Registro de Alumno:" + str(m.getCodigoAlumno()) + "\n")
        archivo.write("nota 1:" + str(m.getnota1()) + "\n")
        archivo.write("nota 2:" + str(m.getNota2()) + "\n")
        archivo.write("nota 3:" + str(m.getNota3()) + "\n")

    archivo.close()

    messagebox.showinfo("Backup", "Se han guardado los datos exitosamente en " + nombreArchivo)


def cargaArchivos(nombreArchivo, bd: BD_Escuela):
    tabla_Materias = T_Materias()

    listaMaterias = []

    bd.setTablaMaterias(T_Materias())
    bd.setCantidadUsuarios(0)
    bd.setTablaAlumnos(T_Alumnos())

    file = open(nombreArchivo, "r")
    texto = file.read()
    lista = texto.split("\n\n")
    datos_generales = lista[0].split("\n")

    # limpio el string de alumnos

    alumnos = lista[1].split("----")
    alumnos = alumnos[1:]
    alumnos = str(alumnos).split("Alumno n°")
    alumnos = alumnos[1:]

    # limpio el string de materias

    materias = lista[2].split("----")
    materias = materias[1:]
    materias = str(materias).split("Materia n°")
    materias = materias[1:]

    # saco datos generales de la base de datos

    cantidad_usuarios = int(datos_generales[0].split(":")[1])
    bd.setCantidadUsuarios(cantidad_usuarios)

    acceso = datos_generales[1].split(":")
    acceso = acceso[1].split(" ")
    acceso = acceso[:-1]
    for i in acceso:
        usuarios = i.split(",")
        usuario = usuarios[0]
        prefijo = usuario[:2]
        nombre = usuario[2:]
        contraseña = usuarios[1]
        if prefijo == "P-":
            bd.RegUs(nombre, contraseña, 2)
        elif prefijo == "D-":
            bd.RegUs(nombre, contraseña, 1)
        elif prefijo == "A-":
            bd.RegUs(nombre, contraseña, 0)

    # Cargamos el diccionario del nombre de las materias
    '''
    nombreTablas = datos_generales[2].split(":")
    nombreTablas = nombreTablas[1].split(" ")
    tabla_alumnos = nombreTablas[0].split(",")
    tabla_materias = nombreTablas[1].split(",")
    

    nombretablas = {tabla_alumnos[0]: tabla_alumnos[1], tabla_materias[0]: tabla_materias[1]}
    
    bd.setNombreTablas(nombretablas)
    '''
    # Cargamos la lista de alumnos

    for i in alumnos:
        a = i.split("\\n")
        nombre = a[1].split(":")
        apellido = a[2].split(":")
        dni = a[3].split(":")
        tel = a[4].split(":")
        email = a[5].split(":")
        fecha = a[6].split(":")
        año = a[7].split(":")
        fecha_alta = a[8].split(":")
        fecha_baja = a[9].split(":")
        us = a[10].split(":")
        concepto = a[11].split(":")
        inasistencias = a[12].split(":")

        a1 = Alumnos(int(a[0]), nombre[1], apellido[1], int(dni[1]), int(tel[1]), email[1], fecha[1], int(año[1]),
                     fecha_alta[1], fecha_baja[1], us[1], concepto[1], int(inasistencias[1][:2]))

        bd.AltaAlumnoBaseDatos(a1)

    # cargamos la lista de materias

    for i in materias:
        m = i.split("\\n")
        num_materia = m[0].split(":")
        nombre_materia = m[1].split(":")
        nro_alumno = m[2].split(":")
        nota1 = m[3].split(":")
        nota2 = m[4].split(":")
        nota3 = m[5].split(":")

        m1 = Materia(nombre_materia[1], nota1[1], nota2[1], nota3[1], int(num_materia[0]), int(nro_alumno[1]))

        listaMaterias.append(m1)

    tabla_Materias.setListaMaterias(listaMaterias)
    bd.setTablaMaterias(tabla_Materias)
    messagebox.showinfo("carga de archivo exitosa","carga de archivo exitosa")


def LisTAlu(bd=BD_Escuela()):
    t_alumnos = bd.getTablaAlumnos()

    root = Tk()
    root.title("Listado de Alumnos")
    root.geometry('1500x200')

    # Etiquetas

    label_norregistro = Label(root, width=10, text="Nro \nRegistro")
    label_nombre = Label(root, text="Nombre y Apellido")
    label_dni = Label(root, width=10, text="DNI")
    label_telefono = Label(root, text="Telefono")
    label_fecha = Label(root, width=10, text="Fecha de\n Nacimiento")
    label_email = Label(root, text="Email")
    label_año = Label(root, text="Curso")
    label_a_fecha = Label(root, width=10, text="Fecha de\n Alta")
    label_b_fecha = Label(root, width=10, text="Fecha de\n Baja")
    label_usuario = Label(root, text="Usuario")
    label_inasistencias = Label(root, text="Inasistencias")
    label_concepto = Label(root, text="Concepto")

    # ListBox (tablas)

    l_nroregistro = Listbox(root, width=10, height=30)
    l_nombres = Listbox(root, height=30)
    l_dni = Listbox(root, width=10, height=30)
    l_telefono = Listbox(root, height=30)
    l_fecha = Listbox(root, width=10, height=30)
    l_email = Listbox(root, height=30)
    l_año = Listbox(root, width=10, height=30)
    l_a_fecha = Listbox(root, width=10, height=30)
    l_b_fecha = Listbox(root, width=10, height=30)
    l_usuario = Listbox(root, height=30)
    l_inasistencias = Listbox(root, height=30)
    l_concepto = Listbox(root, height=30)

    for item in t_alumnos.getListaAlumnos():
        l_nroregistro.insert(0, item.getNroregistro())
        l_nombres.insert(0, item.getnombre() + "  " + item.getApellido())
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
    label_norregistro.grid(row=0, column=1)
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
    label_contraseña = Label(root, width=15, text="Contraseña")
    label_tipo = Label(root, width=15, text="Tipo")

    # ListBox
    l_usuario = Listbox(root, width=15, height=15)
    l_contaseña = Listbox(root, width=15, height=15)
    l_tipo = Listbox(root, width=20, height=15)

    for item in acceso.items():
        l_usuario.insert(0, item[0][2:])
        l_contaseña.insert(0, item[1])
        if item[0][:2] == "P-":
            l_tipo.insert(0, "ADMINISTRADOR")
        elif item[0][:2] == "D-":
            l_tipo.insert(0, "DOCENTE")
        elif item[0][:2] == "A-":
            l_tipo.insert(0, "ALUMNO")

    # acomodalos los componentes
    label_usuario.grid(row=0, column=1)
    label_contraseña.grid(row=0, column=2)
    label_tipo.grid(row=0, column=3)

    l_usuario.grid(row=1, column=1)
    l_contaseña.grid(row=1, column=2)
    l_tipo.grid(row=1, column=3)

    root.mainloop()


def ListMat(base_datos = BD_Escuela()):
    root = Tk()
    root.title("Listado de Materias")
    root.geometry('600x900')
    root.grid()

   # tabla = T_Materias()

    tabla = base_datos.getTablaMaterias()

    # Etiquetas
    label_registro_alumno = Label(root, text="Registro")
    label_CodigoMateria = Label(root, text="Codigo de\n Materia")
    label_Materia1 = Label(root, text="Nombre de la Materia")
    label_nota1 = Label(root, text="nota 1")
    label_nota2 = Label(root, text="nota 2")
    label_nota3 = Label(root, text="nota 3")

    # listBox
    l_registro = Listbox(root, width=10, height=30)
    l_codigo_materia = Listbox(root, width=10, height=30)
    l_materia = Listbox(root, width=20, height=30)
    l_nota1 = Listbox(root, width=10, height=30)
    l_nota2 = Listbox(root, width=10, height=30)
    l_nota3 = Listbox(root, width=10, height=30)

    for item in base_datos.getTablaMaterias().getListaMaterias():
        l_registro.insert(0, item.getCodigoAlumno())
        l_codigo_materia.insert(0, item.getCodigo())
        l_materia.insert(0, item.getnombre())
        l_nota1.insert(0, item.getnota1())
        l_nota2.insert(0, item.getNota2())
        l_nota3.insert(0, item.getNota3())

    # acomodamos

    label_registro_alumno.grid(row=0, column=1)
    label_CodigoMateria.grid(row=0, column=2)
    label_Materia1.grid(row=0, column=3)
    label_nota1.grid(row=0, column=4)
    label_nota2.grid(row=0, column=5)
    label_nota3.grid(row=0, column=6)

    l_registro.grid(row=1, column=1)
    l_codigo_materia.grid(row=1, column=2)
    l_materia.grid(row=1, column=3)
    l_nota1.grid(row=1, column=4)
    l_nota2.grid(row=1, column=5)
    l_nota3.grid(row=1, column=6)

    root.mainloop()


def ListInas(basedatos: BD_Escuela):
    readmision = list(filter(lambda x: x.getInasistencias() > 15, basedatos.getTablaAlumnos().getListaAlumnos()))

    root = Tk()
    root.title("Listado de Alumnos")
    root.geometry('800x400')

    # Etiquetas

    label_nombre = Label(root, text="Nombre y Apellido")
    label_año = Label(root, text="Año")
    label_inasistencias = Label(root, text="Inasistencias")
    label_concepto = Label(root, text="Concepto")

    # ListBox (tablas)

    l_nombres = Listbox(root, height=30)
    l_año = Listbox(root, width=10, height=30)
    l_inasistencias = Listbox(root, height=30)
    l_concepto = Listbox(root, height=30)

    for item in readmision:
        l_nombres.insert(0, item.getnombre() + "  " + item.getApellido())
        l_año.insert(0, item.getAño())
        l_inasistencias.insert(0, item.getInasistencias())
        l_concepto.insert(0, item.getConcepto())

    # acomodamos las etiquetas de las tablas
    label_nombre.grid(row=0, column=1)
    label_año.grid(row=0, column=2)
    label_inasistencias.grid(row=0, column=3)
    label_concepto.grid(row=0, column=4)
    l_nombres.grid(row=1, column=1)
    l_año.grid(row=1, column=2)
    l_inasistencias.grid(row=1, column=3)
    l_concepto.grid(row=1, column=4)
    root.mainloop()


def auxiliar(lista, elemento, curso):
    if elemento[0] == curso:
        for i in lista:
            if i[1].casefold() < elemento[1].casefold():
                lista.insert(lista.index(i), elemento)
                return lista
        lista.append(elemento)
        return lista
    return lista


def alumnos(a: Alumnos):
    return [a.getAño(), a.getnombre(), a.getApellido(), a.getDni(), a.getNroregistro()]


def AAlumno(bdatos, nroRegistro=0, nombre="defecto", apellido="", dni=55, telefono=0, fecha=0, email="hola", anio=0
            , fechaAlta=0, fechaBaja=0, usuario="", concepto="", inasistencias=0):
    a = Alumnos(nroRegistro, nombre, apellido, dni, telefono, email, fecha, anio, fechaAlta, fechaBaja, usuario
                , concepto, inasistencias)
    print(a.getEmail())
    if bdatos.AltaAlumnoBaseDatos(a):
        mensaje = messagebox.showinfo("Alumno Cargado"
                                      ,
                                      "El alumno: " + a.getnombre() + a.getApellido() + " \n ha sido cargado exitosamente")
    else:
        error = messagebox.showerror("Error Registro", "Ya existe un alumno en la base de datos")


def MAlumno(bdatos, nroRegistro=0, nombre="defecto", apellido="", dni=55, telefono=0, fecha="0", email="", año=0
            , fechaAlta="0", fechaBaja="0", usuario="", concepto=" ", inasistencias=0):
    a = Alumnos(nroRegistro, nombre, apellido, dni, telefono, email, fecha, año, fechaAlta, fechaBaja, usuario
                , concepto, inasistencias)
    print(a.getEmail())
    if bdatos.modificarAlumno(a):
        messagebox.showinfo("Alumno Modificado"
                            ,
                            "El alumno: " + a.getnombre() + a.getApellido() + " \n ha sido modificado exitosamente")
    else:
        messagebox.showerror("Error Registro", "Ya existe un alumno en la base de datos")


def CAlumno(bdatos=BD_Escuela(), nro_registro=0):
    tabla = bdatos.getTablaAlumnos()
    a = Alumnos()
    a = tabla.ConsultaAlumno(nro_registro)
    return a


def EAlumno(bdatos=BD_Escuela(), nro_registro=0):
    bdatos.BajaAlumno(nro_registro)
    messagebox.showinfo("Alumno Eliminado",
                        "El Alumno con el numero de registro: " + str(nro_registro) + " Ha sido eliminado exitosamente")


def RegUs(baseDatos: BD_Escuela, nombre, contraseña, tipo):
    if baseDatos.RegUs(nombre, contraseña, tipo):
        messagebox.showinfo("Carga con Exito", "se ha cargado el usuario con exito")
    else:
        messagebox.showerror("usuario existente", "Ya existe ese usuario en el sistema")
