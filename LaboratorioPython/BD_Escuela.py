from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Tablas import T_Alumnos,T_Materias
from tkinter import messagebox


class BD_Escuela():

    def __init__(self):
        self.__cant_usuarios = 0;
        self.__acceso = {}
        self.__NbreTablas={"T_Alumnos": 0, "T_Materias": 1}
        self.__tablas=[T_Alumnos(),T_Materias()]

    def repetidos(self,clave):
        control = False
        for i in self.__acceso.keys():
            if clave == i:
                control = True
        return control

    def RegUs(self,nombre = "nada", passw="?", numero=0):
            if numero == 1: # 1 = carga de Docente
                prefijo = "D-"
                nombreUsuario = prefijo + nombre
                if not (self.repetidos(nombreUsuario)):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios+1

                # colocar el cartel de que el usuario ya esta repetido.

            elif numero == 2: # 2 = carga de Programador
                prefijo = "P-"
                nombreUsuario = prefijo + nombre
                if not (self.repetidos(nombreUsuario)):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios + 1
                    print("exitoso")

            elif numero == 0: # 0 = carga de alumno
                prefijo = "A-"
                nombreUsuario = prefijo + nombre
                if not (self.repetidos(nombreUsuario)):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios=self.__cant_usuarios+1
            else:
                messagebox.showerror("usuario existente", "Ya existe ese usuario en el sistema")


    def ElimUs(self, nombre):
        usuario = list(filter(lambda x: x[0][2:]==nombre,self.__acceso.items()))
        if usuario[0][0][:2] =="D-": # eliminar un docente
            del self.__acceso["D-"+nombre]
        if usuario[0][0][:2] =="P-": # eliminar un pogramador
            del self.__acceso["P-"+nombre]
        if usuario[0][0][:2] =="A-": # eliminar un alumno
            del self.__acceso["A-"+nombre]

    def getAcceso(self):
        return self.__acceso

    def getCantidadAlumnos(self):
        return self.__cant_usuarios

    def getTablaAlumnos(self):
        return self.__tablas[self.__NbreTablas["T_Alumnos"]]

    def setTablaAlumnos(self,tabla= T_Alumnos()):
        self.__tablas[self.__NbreTablas["T_Alumnos"]]=tabla

    def getTablaMaterias(self):
        return self.__tablas[self.__NbreTablas["T_Materias"]]

    def setTablaMaterias(self,tabla= T_Materias):
        self.__tablas[self.__NbreTablas["T_Materias"]]=tabla

    def AltaAlumnoBaseDatos(self,a=Alumnos()):
        if self.__tablas[self.__NbreTablas["T_Alumnos"]].AltaAlumno(a):
            self.RegUs(a.getnombre(),a.getDni(),0)
            return True
        else:
            return False



