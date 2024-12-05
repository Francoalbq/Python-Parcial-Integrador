#Arboles binarios unidad 3:
#Usa un árbol binario de búsqueda para organizar los pacientes de una 
#clínica por su número de identificación médica (ID). Debes permitir 
#inserciones, eliminaciones, y búsquedas eficientes.
import datetime

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def set_izq(self, nodo):
        self.izq = nodo
    
    def set_der(self, nodo):
        self.der = nodo
    
    def valor_nodo(self):
        return self.valor
    
    def valor_izq(self):
        return self.izq
    
    def valor_der(self):
        return self.der

    def insertar(self, valor):
        """
        Insertar un valor en el árbol binario de búsqueda de manera iterativa.
        Se asegura de que el valor se inserte en el lugar correcto.
        """
        nuevo_nodo = Nodo(valor)
        current = self

        while True:
            if valor < current.valor_nodo():
                if current.izq is None:
                    current.set_izq(nuevo_nodo)
                    break
                else:
                    current = current.izq
            elif valor > current.valor_nodo():
                if current.der is None:
                    current.set_der(nuevo_nodo)
                    break
                else:
                    current = current.der
            else:
                break  # Si el valor ya existe, no lo insertamos.

    def buscar(self, valor):
        """
        Buscar un valor en el árbol binario de búsqueda.
        Se devuelve el nodo si se encuentra el valor, o None si no lo encontramos.
        """
        if valor == self.valor_nodo():
            return self
        
        if valor < self.valor_nodo() and self.izq is not None:
            return self.izq.buscar(valor)
        
        if valor > self.valor_nodo() and self.der is not None:
            return self.der.buscar(valor)
        
        return None

    def eliminar(self, valor):
        """
        Elimina un valor del árbol binario de búsqueda.
        Se manejan tres situaciones:
        1. El nodo no tiene hijos o tiene solo uno, en cuyo caso simplemente se elimina.
        2. El nodo tiene dos hijos, por lo que se reemplaza su valor por el más pequeño de su subárbol derecho.
        """
        if valor < self.valor_nodo():
            if self.izq is not None:
                self.set_izq(self.izq.eliminar(valor))
        elif valor > self.valor_nodo():
            if self.der is not None:
                self.set_der(self.der.eliminar(valor))
        else:
            if self.izq is None:
                return self.der
            elif self.der is None:
                return self.izq
            
            minimo = self.der.buscar_minimo()
            self.valor = minimo.valor_nodo()
            self.set_der(self.der.eliminar(minimo.valor_nodo()))
        
        return self

    def buscar_minimo(self):
        current = self
        while current.izq is not None:
            current = current.izq
        return current

    def mostrar_inorden(self):
        if self.izq:
            self.izq.mostrar_inorden()
        print(self.valor_nodo(), end=' ')
        if self.der:
            self.der.mostrar_inorden()


# Creación del árbol y operaciones
arbol = Nodo(10)
arbol.set_izq(Nodo(5))
arbol.set_der(Nodo(35))

arbol.insertar(30)
arbol.insertar(4)
arbol.insertar(8)
arbol.insertar(40)

print("ID de los Pacientes en orden: ")
arbol.mostrar_inorden()

id_buscar = 40
resultado = arbol.buscar(id_buscar)
if resultado:
    print(f"\nEl paciente con ID {id_buscar} fue encontrado.")
else:
    print(f"\nEl paciente con ID {id_buscar} no fue encontrado.")

id_eliminar = 40
arbol.eliminar(id_eliminar)
print(f"\nEliminando paciente con ID {id_eliminar}. Nuevo árbol:")
arbol.mostrar_inorden()

# Calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")