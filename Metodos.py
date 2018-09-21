__autor__ = 'Moises mondragon mondragon'

class Memoria_Dinamica:
    __listas = []

    def __init__(self, list):
        self.__lista = list

    def getlistas(self):
        return self.__listas

    def recorerarreglo(self):
        for x in self.getlists():
            print (self.getlistas().index(x)+1, x)

    def agregarelemtonarray(self, elemento):
        self.__listas.append(elemento)

    def ordenarlista(self):
        self.__listas.sport()

    def eliminarelementos(self, num):
        self.__listas.pop(num)

    def eliminarelemento(self, elemento):
        self.__listas.remove(elemento)

    def imprimirLista(self):
            print(self.__lista)
