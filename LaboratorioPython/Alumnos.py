from LaboratorioPython.Materia import Materia


class Alumnos:
    def __init__(self, nroRegistro=0000, nombre="defectoasd", apellido="-", dni=123123123, telefono=0, email="-", fecha="-",
                 año=0, fechaAlta="0", fechaBaja="0", usuario="-",concepto="A", inasistencias=" 0 "):
        self.__Nro_Registro = nroRegistro
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__email = email
        self.__fecha = fecha
        self.__año = año
        self.__fechaAlta = fechaAlta
        self.__fechaBaja = fechaBaja
        self.__usuario = usuario
        self.__concepto = concepto
        self.__inasistencias = inasistencias
        self.__materias = [Materia("Matematicas", 0, 0, 0, 1), Materia("Lengua", 0, 0, 0, 2),
                           Materia("Física", 0, 0, 0, 3),Materia("Química", 0, 0, 0, 4),
                           Materia("Biología", 0, 0, 0, 5),Materia("Etica", 0, 0, 0, 6),
                           Materia("Geología", 0, 0, 0, 8),Materia("Historia", 0, 0, 0, 7),
                           Materia("Computacion", 0, 0, 0, 9)]

    def getNroregistro(self):
        return self.__Nro_Registro

    def setNroregsitro(self, nroregsitro):
        self.__Nro_Registro = nroregsitro

    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getEmail(self):
        self.__email

    def setEmail(self, email):
        self.__email = email

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha

    def getAño(self):
        return self.__fecha

    def setAño(self, año):
        self.__año = año

    def getFechaAlta(self):
        return self.__fechaAlta

    def setFechaAlta(self, fecha):
        self.__fechaAlta = fecha

    def getFechaBaja(self):
        return self.__fechaBaja

    def setFechaBaja(self, fecha):
        self.__fechaBaja = fecha

    def getUsuario(self):
        return self.__usuario

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getConcepto(self):
        return self.__concepto

    def setConcepto(self, concepto):
        self.__concepto = concepto

    def getInasistencias(self):
        return self.__inasistencias

    def setInasistencias(self, inasistencias):
        self.__inasistencias = inasistencias

    def getMateria(self):
        return self.__materias
'''
    def setMateria(self):
        self.__Materia.append(self, Materia("Matematicas", 0, 0, 0, 1))
        self.__Materia.append(self, Materia("Lengua", 0, 0, 0, 2))
        self.__Materia.append(self, Materia("Física", 0, 0, 0, 3))
        self.__Materia.append(self, Materia("Química", 0, 0, 0, 4))
        self.__Materia.append(self, Materia("Biología", 0, 0, 0, 5))
        self.__Materia.append(self, Materia("Etica", 0, 0, 0, 6))
        self.__Materia.append(self, Materia("Geología", 0, 0, 0, 8))
        self.__Materia.append(self, Materia("Historia", 0, 0, 0, 7))
        self.__Materia.append(self, Materia("Computacion", 0, 0, 0, 9))
'''


