__autor__ = 'Moises mondragon mondragon'

class Memoria_Dinamica:
    __listas = []

    def __init__(self, list):
        self.__lista = list

    def getlistas(self):
        return self.__listas

    def recorerarreglo(self):
        for x in self.getlistas():
            print (self.getlistas().index(x)+1, x)

    def agregarelementoarray(self, elemento):
        self.__listas.append(elemento)

    def eliminarelementos(self, num):
        self.__listas.pop(num)

    def imprimirLista(self):
            print(self.__lista)
