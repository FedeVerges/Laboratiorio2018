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
        lista=list(filter(lambda x: x.getNroregistro()==NroRegistro,self.__listaAlumnos))
        if lista ==[]:
            return False
        else:
            lista[0].getNroregistro()
            self.__listaAlumnos.remove(lista[0])
            return True


        # eliminar materias

    def ModificacionAlumno(self,a = Alumnos()):
        for al in self.__listaAlumnos:
            if a.getNroregistro() == al.getNroregistro():
                self.__listaAlumnos[self.__listaAlumnos.index(al)] = a
                return True
            else:
                error = "no existe un usuario con ese nombre"
                print(error)
                return False

    def ConsultaAlumno(self,NroRegistro):
        for i in self.__listaAlumnos:
            if NroRegistro == i.getNroregistro():
                return i
            else:
                return False

    def legajo(self,dni):
        alumnos = list(filter(lambda x: x.getDni()== dni, self.__listaAlumnos))
        if alumnos ==[]:
            return False
        else:
            return alumnos[0]

    def getListaAlumnos(self):
        return self.__listaAlumnos




class T_Materias:
    def __init__(self):
        self.__listaMaterias=[Materia()]
        self.__tabla={}

    def AltaMat(self, m = Materia()):
        self.__listaMaterias.append(m)

    def BajaMat(self,nro_registro):
        lista = list(filter(lambda x: x.getCodigoAlumno()==nro_registro, self.__listaMaterias))
        for i in lista:
            self.__listaMaterias.remove(i)
            print("borrado")
    def ModificacionMat(self,m = Materia()):
        for i in self.__listaMaterias:
            if m.getCodigo() == i.getCodigo():
                self.__listaMaterias[self.__listaMaterias.index(i)]= m

    def ConsultaMat(self, nro_registro,cod_materia):
        lista = list(filter(lambda x: x.getCodigoAlumno()==nro_registro, self.__listaMaterias))
        print(lista)
        for i in lista:
            if i.getCodigo()==cod_materia:
                return i
            else:
                print("el alumno no tiene materias")


    def ConsultLegajo(self,nro_registro):
        lista = list(filter(lambda x: x.getCodigoAlumno() == nro_registro, self.__listaMaterias))
        return lista



    def getListaMaterias(self):
        return self.__listaMaterias

    def serListaMaterias(self, lista):
        self.__listaMaterias= lista




