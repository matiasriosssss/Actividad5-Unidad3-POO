import zope.interface
from zope.interface import implementer
import numpy as np

class Ipruebas(zope.interface.Interface):
    def insertarElemento(self, indice, elemento):
        pass
    def agregarElemento(self, elemento):
        pass
    def mostrarElemento(self, posicion):
        pass

@implementer(Ipruebas)
class listaa:
    def __init__(self, lis):
        self.list = lis
    def insertarElemento(self, indice, elemento):
        if indice > 0 and indice < len(self.list):
            self.list.insert(indice, elemento)
            print(f"Nueva lista: {self.list}")
        else:
            print("El indice supera a la cantidad de componentes...")
    def agregarElemento(self, elemento):
        self.list.append(elemento)
        print(f"Nueva lista {self.list}")
    def mostrarElemento(self, posicion):
        try:
            print(f"{self.list[posicion]}")
        except IndexError:
            print("No se puede mostrar el elemento de la lista debido a que la posicion no es valida...")
    

@implementer(Ipruebas)
class arregloo:
    def __init__ (self, arre):
        self.arreglo = arre
    def insertarElemento(self, indice, elemento):
        if indice < len(self.arreglo):
            newA = np.insert(self.arreglo, indice, elemento)
            self.arreglo = newA
            del newA
            print(f"Nuevo arreglo: {self.arreglo}")
        else:
            print("El indice supera a la cantidad de componentes...")
                    
    def agregarElemento(self, elemento):
        newArre = np.append(self.arreglo, elemento)
        self.arreglo = newArre
        del newArre
        print(f"Nuevo arreglo: {self.arreglo}")
        
    def mostrarElemento(self, posicion):
        try:
            print(f"{self.arreglo[posicion]}")
        except IndexError:
            print("No se puede mostrar el elemento del arreglo debido a que la posicion no es valida...")
def test():
    lista = [1,3,5,7,9,11,13,15]
    arreglo = np.array([2,4,6,8,10,12,14])
    p1 = listaa(lista)
    p2 = arregloo(arreglo)
    p1.insertarElemento(1, 2)
    p2.insertarElemento(4,9)
    p2.insertarElemento(8,15)
    
    p1.agregarElemento(17)
    p2.agregarElemento(16)
    
    p1.mostrarElemento(4)
    p2.mostrarElemento(8)
    p1.mostrarElemento(15)
    p2.mostrarElemento(32)

    
if __name__ == '__main__':
    test()