#Grafos (Unidad 7):
#Modela la red de hospitales y clínicas como un grafo. Los nodos representan 
#hospitales y las aristas las conexiones entre ellos (distancias o tiempos de 
#transferencia de pacientes)
import datetime

class Directed_Graph:    
    def __init__(self):
        self.graph_dict = {}  #Contiene los nodos del grafo
        
    def add_vertex(self, vertex):
        if vertex in self.graph_dict:       # Evitar añadir dos vertices al mismo tiempo
            return "Vertex alredy in graph"  
        self.graph_dict[vertex] = []        # Agrega un vertice al diccionario/grafo
        
        
    def add_edge(self, edge):  # Agregar conexiones entre los vertices
        v1 = edge.get_v1()   
        v2 = edge.get_v2()
        if v1 not in self.graph_dict: # Evitar errores en caso de que no exista el grafo
            raise ValueError(f'Vertice {v1.get_name()} no esta en el grafo') 
        if v2 not in self.graph_dict:                                        
            raise ValueError(F'Vertice {v2.get_name()} no esta en el grafo')
        
        self.graph_dict[v1].append(v2)   #Agregar una nueva conexion al diccionario/grafo
    
    
    'Funciones del grafo'
   
    #Obtener los vecinos del nodo m
    def get_vecinos(self, vertex):
        return self.graph_dict[vertex]
    
    #Verificar si un nodo esta en el grafo
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict  
    
    #Devolver un objeto de tipo nodo
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v 
        print(f'El vertice {vertex_name} no existe') 
        return None
         
         
    #Funcion que permite imprimir el grafo
    def __str__(self):
        all_edges = ''  
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + ' ----> ' + v2.get_name() + '\n'  
        return all_edges
    
#Grafo no dirigido    
class Undirected_graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1()) #se crea una nueva arista que va desde el vertice destico hacia el vertice origen
        Directed_Graph.add_edge(self, edge_back)
              
class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1 # vertice origen
        self.v2 = v2 # vertice destino
        self.weight = weight
        
    def get_v1(self):   # Los getters devolveran el valor de los vertices origen-destino
        return self.v1
    def get_v2(self):   
        return self.v2
    
    def get_weight(self):  # Devolvera la distancia de la arist
        return self.weight
    
    def __str__(self): # Imprime los valores de los vertices origen-destino
        return f"{self.v1.get_name()} ---> {self.v2.get_name()}" 
    
class Vertex: 
    def __init__(self, name):
        self.name = name      # Asignamos el nombre del vetice
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name

def build_graph(graph): 
    g = graph()      # indico el tipo de grafo (dirigido-no dirigido)
    for v in ('Hospital Burzaco', 'Hospital Claypole','Hospital Adrogue', 'Hospital Calzada', 'Hospital Temperley', 
              'Hospital Lanus', 'Hospital Don Orione', 'Hospital Malvinas Argentinas', 'Clinica Lomas de Zamora', 
              'Clinica De Niños'):  # Defino los nombres de los vertices
                    g.add_vertex(Vertex(v))
                    
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
    
G1 = build_graph(Undirected_graph) # Para cambiar a Grafo dirigido ---> Directed_graph
print(G1)



# Calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")