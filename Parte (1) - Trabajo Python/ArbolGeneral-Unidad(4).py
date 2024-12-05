#Arboles Generales
# Modela el historial clínico de cada paciente como un árbol general donde 
#cada nodo es un evento médico (consulta, diagnóstico, tratamiento) y las 
#ramas conectan las visitas y tratamientos asociados.
import datetime

class Nodo:
    def __init__(self, valor):   
        self.valor = valor  
        self.hijos = []  
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
    
    def valor_nodo(self):
        return self.valor
    
    def mostrar_hijos(self):
        return [(hijo.valor_nodo()) for hijo in self.hijos]
    
    def recorrer_orden(self):
        for hijo in self.hijos:
            hijo.recorrer_orden()
        print(self.valor, end=' ')
    

historial_clinico = Nodo('Historial Clinico')

consulta = Nodo('Consultas')
diagnostico = Nodo('Diagnosticos')
tratamiento = Nodo('Tratamientos')
consulta_paciente = Nodo('Juan Tolosa 23/02/24')
diagnostico_paciente = Nodo('Covid 19')
tratamiento_paciente = Nodo('Paracetamol 20mg')

historial_clinico.agregar_hijo(consulta)
historial_clinico.agregar_hijo(diagnostico)
historial_clinico.agregar_hijo(tratamiento)
consulta.agregar_hijo(consulta_paciente)
diagnostico.agregar_hijo(diagnostico_paciente)
tratamiento.agregar_hijo(tratamiento_paciente)

# Mostrar la información del nodo raíz y sus hijos
print(historial_clinico.valor_nodo())
print(f'Hijos del historial clinico: {historial_clinico.mostrar_hijos()}')
print(f'hijo de la consulta: {consulta.mostrar_hijos()}')
print(f'Hijo de Diagnostico: {diagnostico.mostrar_hijos()}')
print(f'Hijo de Tratamientos: {tratamiento.mostrar_hijos()}')

historial_clinico.recorrer_orden()

# Calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")