#Problemas NP y Camino Mínimo (Unidad 10):
#Analiza el problema del camino mínimo entre varios hospitales utilizando el 
#algoritmo de Dijkstra para encontrar la mejor ruta para una ambulancia que 
#necesita trasladar a un paciente crítico.


import datetime
import heapq  

class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(edge)  # se guarda la arista en vez de solo el vértice

    def get_vecinos(self, vertex):
        return self.graph_dict[vertex]  # retorna las aristas

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')
        return None

    def get_edge_weight(self, v1, v2):
        # Buscar la arista entre v1 y v2 para obtener su peso
        for edge in self.graph_dict[v1]:
            if edge.get_v2() == v2:
                return edge.get_weight()
        return float('inf')  # si no existe la arista, devuelve infinito

class Vertex:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1  # origen
        self.v2 = v2  # destino
        self.weight = weight  # peso de la arista
    
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        return f"{self.v1.get_name()} ---> {self.v2.get_name()} (Distancia: {self.weight} km)"


def build_graph():
    g = Directed_Graph()
    
    hospitales = [
        'Hospital Burzaco', 'Hospital Claypole', 'Hospital Adrogue', 'Hospital Calzada', 'Hospital Temperley', 
        'Hospital Lanus', 'Hospital Don Orione', 'Hospital Malvinas Argentinas', 'Clinica Lomas de Zamora', 'Clinica De Niños'
    ]
    for h in hospitales:
        g.add_vertex(Vertex(h))

    # Crear aristas con distancias (en kilómetros)
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Claypole'), weight=5))  
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Adrogue'), weight=7))   
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Calzada'), weight=10))  
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Lanus'), weight=12))    
    g.add_edge(Edge(g.get_vertex('Hospital Claypole'), g.get_vertex('Hospital Adrogue'), weight=3))  
    g.add_edge(Edge(g.get_vertex('Hospital Claypole'), g.get_vertex('Hospital Don Orione'), weight=4))  
    g.add_edge(Edge(g.get_vertex('Hospital Adrogue'), g.get_vertex('Hospital Calzada'), weight=6))  
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Lanus'), weight=8))  
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Temperley'), weight=7))  
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Malvinas Argentinas'), weight=9))  
    g.add_edge(Edge(g.get_vertex('Hospital Lanus'), g.get_vertex('Clinica Lomas de Zamora'), weight=6))  
    g.add_edge(Edge(g.get_vertex('Hospital Lanus'), g.get_vertex('Hospital Temperley'), weight=5))  
    g.add_edge(Edge(g.get_vertex('Clinica Lomas de Zamora'), g.get_vertex('Clinica De Niños'), weight=2))  
    g.add_edge(Edge(g.get_vertex('Hospital Temperley'), g.get_vertex('Hospital Malvinas Argentinas'), weight=4))  
    
    return g


# Algoritmo de Dijkstra para encontrar el camino mínimo
def camino_minimo(grafo, origen):
    distancia = {v: float('inf') for v in grafo.graph_dict}  
    padre = {v: None for v in grafo.graph_dict}  
    distancia[origen] = 0  
    q = []
    heapq.heappush(q, (0, origen)) 
    while q:
        dist, v = heapq.heappop(q)
        if dist > distancia[v]:
            continue

        for edge in grafo.get_vecinos(v):
            w = edge.get_v2()  
            weight = edge.get_weight() 
            new_dist = distancia[v] + weight
            if new_dist < distancia[w]:
                distancia[w] = new_dist
                padre[w] = v
                heapq.heappush(q, (new_dist, w))

    return padre, distancia


G1 = build_graph()
origen = G1.get_vertex('Hospital Burzaco')
destino = G1.get_vertex('Clinica De Niños')
padre, distancia = camino_minimo(G1, origen)
print(f"Distancia mínima desde {origen.get_name()} hasta {destino.get_name()}: {distancia[destino]} km")

# mostrar el camino recorrido entre el nodo origen y el nodo destino despues de ejecutar el algoritmo de Dijkstra.
camino = []
current = destino
while current:
    camino.append(current.get_name())
    current = padre[current]
camino.reverse()

# imprimir el camino recorrido
print(" Camino recorrido: -> ".join(camino))


# calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")