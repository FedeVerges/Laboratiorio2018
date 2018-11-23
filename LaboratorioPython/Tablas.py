from LaboratorioPython.Alumnos import Alumnos
from LaboratorioPython.Materia import Materia
import time




class T_Alumnos:

    def __init__(self):
        self.__listaAlumnos = []


    def AltaAlumno(self, a = Alumnos()):
        lista=list(filter(lambda x: x.getDni() ==a.getDni(),self.__listaAlumnos))
        if lista==[]:
            self.__listaAlumnos.append(a)
            return True
        else:
            return False

    def BajaAlumno(self,NroRegistro):
        hoy = time.strftime("%d/%m/%y")

        lista=list(filter(lambda x: x.getNroregistro() == NroRegistro,self.__listaAlumnos))
        if lista ==[]:
            return False
        else:
            lista[0].setFechaBaja(hoy)
            lista[0].setnombre(lista[0].getnombre()+" BAJA")
            return True


        # eliminar materias

    def ModificacionAlumno(self,a = Alumnos()):
        for al in self.__listaAlumnos:
            if a.getNroregistro() == al.getNroregistro():
                # self.__listaAlumnos[self.__listaAlumnos.index(al)]
                al.setnombre(a.getnombre())
                al.setApellido(a.getApellido())
                al.setDni(a.getDni())
                al.setTelefono(a.getTelefono())
                al.setEmail(a.getEmail())
                al.setFecha(a.getFecha())
                al.setAño(a.getAño())
                al.setFechaAlta(a.getFechaAlta())
                al.setFechaBaja(a.getFechaBaja())
                al.setUsuario(a.getUsuario())
                al.setConcepto(a.getConcepto())
                al.setInasistencias(a.getInasistencias())
                return True
            else:
                return False

    def ConsultaAlumno(self,NroRegistro):
        for i in self.__listaAlumnos:
            if NroRegistro == i.getNroregistro():
                return i
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
        self.__listaMaterias = []

    def AltaMat(self, m = Materia()):
        self.__listaMaterias.append(m)

    def BajaMat(self,nro_registro):
        lista = list(filter(lambda x: x.getCodigoAlumno()==nro_registro, self.__listaMaterias))
        for i in lista:
            i.setNombre(i.getnombre()+" BAJA")

    def ModificacionMat(self,m = Materia()):
        for i in self.__listaMaterias:
            if m.getCodigo() == i.getCodigo():
                self.__listaMaterias[self.__listaMaterias.index(i)]= m
                return True

    def ConsultaMat(self, nro_registro,cod_materia):
        lista = list(filter(lambda x: x.getCodigoAlumno()==nro_registro, self.__listaMaterias))
        print(lista)
        for i in lista:
            if i.getCodigo()==cod_materia:
                return i

        print("el alumno no tiene materias")


    def ConsultLegajo(self,nro_registro):
        lista = list(filter(lambda x: x.getCodigoAlumno() == nro_registro, self.__listaMaterias))
        return lista



    def getListaMaterias(self):
        return self.__listaMaterias

    def setListaMaterias(self, lista):
        self.__listaMaterias= lista




