from tkinter import *
from tkinter import ttk,Tk

from LaboratorioPython.BD_Escuela import BD_Escuela
from LaboratorioPython.Funcionalidades import *
from LaboratorioPython.Alumnos import *
class Principal():

    def ventanaAltaAlumno(self,bdatos):

        self.ventana = Tk()
        self.ventana.geometry("400x600")

        # variables

        self.nroregistro = bdatos.getCantidadAlumnos() + 1
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

        label_nombre = Label(self.ventana, text="Nombre:")
        label_apellido = Label(self.ventana, text="Apellido:")
        label_dni = Label(self.ventana, text="DNI:")
        label_telefono = Label(self.ventana, text="Telefono:")
        label_fecha = Label(self.ventana, text="Fecha de Nacimiento:")
        label_email = Label(self.ventana, text="Email:")
        label_año = Label(self.ventana, text="Año:")
        label_a_fecha = Label(self.ventana, text="Fecha de Alta:")
        label_usuario = Label(self.ventana, text="Usuario:")
        label_concepto = Label(self.ventana, text="Concepto:")
        label_inasistencias = Label(self.ventana, text="Inasistencias:")

        # Creacion de los campos de texto

        self.texto_nombre = Entry(self.ventana, textvariable=self.nombre, width=30)
        texto_apellido = Entry(self.ventana, textvariable=self.apellido, width=30)
        texto_dni = Entry(self.ventana, textvariable=self.dni, width=30)
        texto_telefono = Entry(self.ventana, textvariable=self.telefono, width=30)
        texto_fecha = Entry(self.ventana, textvariable=self.fechaNacimiento, width=30)
        texto_email = Entry(self.ventana, textvariable=self.email, width=30)
        texto_año = Entry(self.ventana, textvariable=self.año, width=30)
        texto_a_fecha = Entry(self.ventana, textvariable=self.fechaAlta, width=30)
        texto_usuario = Entry(self.ventana, textvariable=self.usuario, width=30)
        texto_concepto = Entry(self.ventana, textvariable=self.concepto, width=30)
        texto_inasistencias = Entry(self.ventana, textvariable=self.inasistencias, width=30)

        # Creacion de botones

        # boton_aceptar = Button(self.ventana, text="Aceptar", command=lambda: AAlumno(bdatos,nroregistro,nombre.get(),apellido.get(),dni.get(),telefono.get(),fechaNacimiento.get(),email.get(),año.get(),fechaAlta.get(),fechaBaja.get(),usuario.get(),inasistencias.get(),concepto.get()))
        boton_modificar = Button(self.ventana, text="Modificar", command=lambda: print(self.nombre.get()))
        boton_elimiar = Button(self.ventana, text="eliminar")

        label_nombre.pack(side=TOP)
        self.texto_nombre.pack(side=TOP)

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

        self.ventana.mainloop()






def main ():
    bdatos = BD_Escuela()
    bdatos.RegUs("fede","1234",2)
    a = Alumnos(3500,"juan","perez",41221770,2664372050,"armando@jofre@gmail.com","16/06/1998",4,"2005","0","juan","MA",10)
    a2 = Alumnos(1200,"jose","Di Marco","3028516",1155664461,"j_Dmarco@mail.com","16/09,1935",1,"2003","0","jose35","NA",10)



    '''p = T_Alumnos()
    p = bdatos.getTablaAlumnos()
    p.AltaAlumno(a)
    p.AltaAlumno(a2)
    p.AltaAlumno(a2)
    BackAlumnos(bdatos)
    '''
   ##  ventanaAltaAlumno(bdatos)

    return 0

if __name__ == '__main__':
    main()




