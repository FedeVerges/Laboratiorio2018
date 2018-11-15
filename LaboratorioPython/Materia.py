
class Materia():
    def __init__(self,nombre=" ", nota1="0",nota2="0",nota3="0", codigo="0"):
        self.__nombre = nombre
        self.__nota1=nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
        self.__codigo=codigo

    def getnombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre= nombre

    def getnota1(self):
        return self.__nota1

    def setNota1(self, nota):
        self.__nota1 = nota

    def getNota2(self):
        return self.__nota2

    def setNota2(self, nota):
        self.__nota2 = nota

    def getNota3(self):
        return self.__nota3

    def setNota3(self, nota):
        self.__nota3 = nota

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self,codigo):
        self.__codigo=codigo


