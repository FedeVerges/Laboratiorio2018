from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Materia import Materia
from LaboratorioPython.Tablas import T_Alumnos, T_Materias
from tkinter import messagebox


class BD_Escuela():

    def __init__(self):
        self.__cant_usuarios = 0;
        self.__acceso = {}
        self.__NbreTablas = {'T_Alumnos': 0, 'T_Materias': 1}
        self.__tablas = [T_Alumnos(), T_Materias()]

    def no_repetidos(self, clave):
        control = False
        lista = list(filter(lambda x: x == clave, self.__acceso.keys()))
        if lista == []:
            control = True
        return control

    def RegUs(self, nombre="nada", passw="?", numero=-1,archivo=0):
        if archivo == 0:
            if numero == 1:  # 1 = carga de Docente
                prefijo = "D-"
                nombreUsuario = prefijo + nombre
                if self.no_repetidos(nombreUsuario):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios + 1
                    return True
                else:
                    return False

            elif numero == 2:  # 2 = carga de Programador
                prefijo = "P-"
                nombreUsuario = prefijo + nombre
                if self.no_repetidos(nombreUsuario):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios + 1
                    return True
                else:
                    return False

            elif numero == 0:  # 0 = carga de alumno
                prefijo = "A-"
                nombreUsuario = prefijo + nombre
                if not self.no_repetidos(nombreUsuario):
                    return False
                else:
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios = self.__cant_usuarios + 1
                    return True
            else:
                messagebox.showerror("Error al cargar Usuario",
                                     "No se ha podido cargar el usuario, controle si faltan campos.")
        else:
            if numero == 1:  # 1 = carga de Docente
                prefijo = "D-"
                nombreUsuario = prefijo + nombre
                if self.repetidos(nombreUsuario):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios + 1
                else:
                    return False

            elif numero == 2:  # 2 = carga de Programador
                prefijo = "P-"
                nombreUsuario = prefijo + nombre
                if self.no_repetidos(nombreUsuario):
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios + 1
                else:
                    return False


            elif numero == 0:  # 0 = carga de alumno
                prefijo = "A-"
                nombreUsuario = prefijo + nombre
                if not self.no_repetidos(nombreUsuario):
                    messagebox.showerror("usuario existente", "Ya existe ese usuario en el sistema")
                else:
                    self.__acceso[nombreUsuario] = passw
                    self.__cant_usuarios = self.__cant_usuarios + 1

            else:
                messagebox.showerror("Error al cargar Usuario",
                                     "No se ha podido cargar el usuario, controle si faltan campos.")


    def ElimUs(self, nombre):
        usuario = list(filter(lambda x: x[0][2:] == nombre, self.__acceso.items()))
        if usuario == []:
            messagebox.showerror("Usuario Inexistente", "No existe paciente en la base de datos")
        elif usuario[0][0][:2] == "D-":  # eliminar un docente
            del self.__acceso["D-" + nombre]
            messagebox.showinfo("Usuario eliminado", "Se ha eliminado el usuario con exito")
        elif usuario[0][0][:2] == "P-":  # eliminar un pogramador
            del self.__acceso["P-" + nombre]
            messagebox.showinfo("Usuario eliminado", "Se ha eliminado el usuario con exito")
        elif usuario[0][0][:2] == "A-":  # eliminar un alumno
            del self.__acceso["A-" + nombre]
            messagebox.showinfo("Usuario eliminado", "Se ha eliminado el usuario con exito")

    def getAcceso(self):
        return self.__acceso

    def getCantidadusuarios(self):
        return self.__cant_usuarios

    def getNombreTablas(self):
        return self.__NbreTablas

    def setNombreTablas(self, nombreTablas):
        self.__NbreTablas = nombreTablas

    def setCantidadUsuarios(self, cant):
        self.__cant_usuarios = cant

    def getNombreTablas(self):
        return self.__NbreTablas

    def getTablaAlumnos(self):
        return self.__tablas[int(self.__NbreTablas['T_Alumnos'])]

    def setTablaAlumnos(self, tabla=T_Alumnos()):
        self.__tablas[int(self.__NbreTablas['T_Alumnos'])] = tabla

    def getTablaMaterias(self):
        print(self.__tablas[int(self.__NbreTablas['T_Materias'])])
        return self.__tablas[int(self.__NbreTablas['T_Materias'])]

    def setTablaMaterias(self, tabla=T_Materias):
        self.__tablas[(self.__NbreTablas['T_Materias'])] = tabla

    def AltaAlumnoBaseDatos(self, a=Alumnos(),archivo = 0):

        if(a.getNroregistro() == 0):
            nroRegistro = self.__cant_usuarios + 1
            a.setNroregsitro(nroRegistro)
        if self.__tablas[int(self.__NbreTablas['T_Alumnos'])].AltaAlumno(a):
            self.RegUs(a.getnombre(), a.getDni(), 0)

            m = [Materia("Matematicas", 0, 0, 0, 1, a.getNroregistro()), Materia("Lengua", 0, 0, 0, 2, a.getNroregistro()),
                 Materia("Física", 0, 0, 0, 3, a.getNroregistro()), Materia("Química", 0, 0, 0, 4, a.getNroregistro()),
                 Materia("Biología", 0, 0, 0, 5, a.getNroregistro()), Materia("Etica", 0, 0, 0, 6, a.getNroregistro()),
                 Materia("Geología", 0, 0, 0, 7, a.getNroregistro()), Materia("Historia", 0, 0, 0, 8, a.getNroregistro()),
                 Materia("Computacion", 0, 0, 0, 9, a.getNroregistro())]
            for i in m:
                self.__tablas[int(self.__NbreTablas['T_Materias'])].AltaMat(i)

            return True
        else:
            return False

    def modificarAlumno(self, a=Alumnos()):
        return self.__tablas[int(self.__NbreTablas['T_Alumnos'])].ModificacionAlumno(a)

    def BajaAlumno(self, nroRegistro):
        a = self.__tablas[int(self.__NbreTablas['T_Alumnos'])].ConsultaAlumno(nroRegistro)
        self.ElimUs(a.getnombre())
        if self.__tablas[int(self.__NbreTablas['T_Alumnos'])].BajaAlumno(nroRegistro):
            self.__tablas[int(self.__NbreTablas['T_Materias'])].BajaMat(nroRegistro)
