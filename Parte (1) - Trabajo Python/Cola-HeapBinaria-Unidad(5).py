#-Cola de Prioridades y Heap Binaria (Unidad 5): 
#Utiliza una cola de prioridades para gestionar la urgencia de los pacientes.  
#Los pacientes más críticos deben ser atendidos primero, basándote en la 
#gravedad de su condición.

import datetime
import heapq 

class Paciente:
    def __init__(self, nombre, gravedad, id_paciente):
        self.nombre = nombre  
        self.gravedad = gravedad  
        self.id_paciente = id_paciente 

    def __str__(self):
        return f"{self.nombre} (Gravedad: {self.gravedad})"
   
    def __lt__(self, otro_paciente):
        if self.gravedad == otro_paciente.gravedad:
            return self.id_paciente < otro_paciente.id_paciente  # FIFO en caso de igualdad
        return self.gravedad > otro_paciente.gravedad  # Prioriza mayor gravedad

def gestion_pacientes(pacientes, id_buscar=None):
    heap = []  
    heapq.heapify(heap)  
    
    for paciente in pacientes:
        print(f'Pacientes en sala de espera: {paciente}')
        heapq.heappush(heap, paciente)  
    print()

    if id_buscar is not None:
        # Llamada a la función de búsqueda en el heap
        paciente_encontrado = buscar_paciente_en_heap(heap, id_buscar)
        if paciente_encontrado:
            print(f"\nPaciente encontrado en la cola de prioridad: {paciente_encontrado}")
        else:
            print(f"\nPaciente con ID {id_buscar} no encontrado en la cola de prioridad.")
    
    atendidos = []  
    
    while heap:
        paciente_atendido = heapq.heappop(heap)
        atendidos.append(paciente_atendido)
        print(f"Atendiendo por orden de gravedad: {paciente_atendido}")
    return atendidos

def buscar_paciente_en_heap(heap, id_buscar):
    for paciente in heap:
        if paciente.id_paciente == id_buscar:
            return paciente
    return None

# Ejemplo de uso
paciente1 = Paciente("Lucas", 3, 1)  
paciente2 = Paciente("Daniel", 5, 2) 
paciente3 = Paciente("German", 2, 3) 
paciente4 = Paciente("Pablo", 7, 4)   

# Crear una lista de pacientes con sus respectivas gravidades y IDs
pacientes = [paciente1, paciente2, paciente3, paciente4]

# Llamar a la función para gestionar la atención de los pacientes
id_a_buscar = 3  # Especifica el ID que quieres buscar
atendidos = gestion_pacientes(pacientes, id_a_buscar)

# Calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")