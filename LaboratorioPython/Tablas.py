from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Materia import Materia


class T_Alumnos:

    def __init__(self):
        self.__listaAlumnos=[]


    def AltaAlumno(self, a = Alumnos()):
        lista=list(filter(lambda x: x.getDni() ==a.getDni(),self.__listaAlumnos))
        print(lista)
        if lista==[]:
            self.__listaAlumnos.append(a)
            return True
        else:
            print("ALUMNO YA EXISTENTE EN EL SISTEMAA!!")
            return False

    def BajaAlumno(self,NroRegistro):
        for i in self.__listaAlumnos:
            if NroRegistro == i.getNroregistro():
                self.__listaAlumnos.remove(i)

    def ModificacionAlumno(self,a = Alumnos()):
        for al in self.__listaAlumnos:
            if a.getNroregistro() == al.getNroregistro():
                self.__listaAlumnos[self.__listaAlumnos.index(al)] = a
            else:
                error = "no existe un usuario con ese nombre"
                print(error)

    def ConsultaAlumno(self,NroRegistro):
        for i in self.__listaAlumnos:
            if NroRegistro == i.getNroregistro():
                return i



    def getListaAlumnos(self):
        return self.__listaAlumnos




class T_Materias:
    def __init__(self):
        self.__listaMaterias=[]

    def AltaMat(self, m = Materia()):
        self.__listaMaterias.append(m)

    def BajaMat(self,nombre):
        for i in self.__listaMaterias:
            if nombre == i.getnombre():
                self.__listaMaterias.remove(i)

    def ModificacionMat(self,m = Materia()):
        for i in self.__listaMaterias:
            if m.getnombre() == i.getnombre():
                self.__listaMaterias[self.__listaMaterias.index(i)]= m
    def ConsultaMat(self, nombre):
        for i in self.__listaMaterias:
            if nombre == i.getnombre():
                return i



    def getListaMaterias(self):
        return self.__listaMaterias




