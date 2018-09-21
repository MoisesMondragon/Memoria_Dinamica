__autor__ = 'Moises mondragon mondragon'
from Metodos import*

ListasMexicanas = []
Mercado_viejo = ['limon','tomate', 'platano', 'pan', 'fresas']
Bebidas = ['cocacola', 'peña fiel', 'pepssi, fanta']
precios = [12, 34, 45, 47]


lista1 = Memoria_Dinamica(Mercado_viejo)
lista1.imprimirLista()
lista1.imprimirLista()
lista1.agregarelementoarray('naranja')
lista1.imprimirLista()

lista2 = Memoria_Dinamica(precios )
lista2.imprimirLista()
lista2.agregarelementoarray(89)
lista2.imprimirLista()

lista3 = Memoria_Dinamica(Bebidas)
lista3.imprimirLista()
lista3.agregarelementoarray('mescal')
lista3.imprimirLista()