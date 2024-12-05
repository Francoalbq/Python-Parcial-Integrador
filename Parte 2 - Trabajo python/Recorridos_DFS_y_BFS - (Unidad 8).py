#Recorridos DFS y BFS (Unidad 8):
#Implementa un algoritmo DFS y BFS para encontrar el camino más corto 
#entre hospitales para transferir un paciente en caso de emergencia.
import datetime

class Directed_Graph:    
    def __init__(self):
        self.graph_dict = {}
        
    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "Vertex alredy in graph"  
        self.graph_dict[vertex] = []
        
    def add_edge(self, edge):
        v1 = edge.get_v1()   
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:                               #Manejo de errores en el caso de que no exista/encuentre el nodo
            raise ValueError(F'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)   #Agregar un nuevo nodo a la lista
    
    #Obtener los vecinos del nodo
    def get_vecinos(self, vertex):
        return self.graph_dict[vertex]
    
    #Verificar si un nodo esta en el grafo
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict #Verificar si la llave vertex esta en el diccionario 
    
    #Devolver un objeto de tipo nodo
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v # Si vertex_name es igual al nombre de alguno de los vertices entonces devolvemos el vertice
        print(f'Vertex {vertex_name} does not exist') # De lo contrario, Devuelve que no existe
        return None
         
    #Funcion que permite imprimir el grafo
    def __str__(self):
        all_edges = ''   #Guardar todas las aristas
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + ' ----> ' + v2.get_name() + '\n'  #Obtener el nombre del nodo origen
        return all_edges
        
class Undirected_graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        Directed_Graph.add_edge(self, edge_back)
              
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1 # origen
        self.v2 = v2 # destino
    def get_v1(self):
        return self.v1
    def get_v2(self): #Devolver el valor
        return self.v2
    def __str__(self): #Hacer un print directamente del objeto
        return self.v1.get_name() + ' ---> ' + self.v2.get_name() #Dirige del nodo 1 al nodo 2
    
class Vertex: #Devuelve el nombre del vertice
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name

def build_graph(graph):
    g = graph()
    for v in ('Hospital Burzaco', 'Hospital Claypole','Hospital Adrogue', 'Hospital Calzada', 'Hospital Temperley', 'Hospital Lanus', 'Hospital Don Orione', 'Hospital Malvinas Argentinas', 'Clinica Lomas de Zamora', 'Clinica De Niños'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Claypole')))
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Adrogue')))
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Calzada')))
    g.add_edge(Edge(g.get_vertex('Hospital Burzaco'), g.get_vertex('Hospital Lanus')))
    g.add_edge(Edge(g.get_vertex('Hospital Claypole'), g.get_vertex('Hospital Adrogue')))
    g.add_edge(Edge(g.get_vertex('Hospital Claypole'), g.get_vertex('Hospital Don Orione')))
    g.add_edge(Edge(g.get_vertex('Hospital Adrogue'), g.get_vertex('Hospital Calzada')))
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Lanus')))
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Temperley')))
    g.add_edge(Edge(g.get_vertex('Hospital Calzada'), g.get_vertex('Hospital Malvinas Argentinas')))
    g.add_edge(Edge(g.get_vertex('Hospital Lanus'), g.get_vertex('Clinica Lomas de Zamora')))
    g.add_edge(Edge(g.get_vertex('Hospital Lanus'), g.get_vertex('Hospital Temperley')))
    g.add_edge(Edge(g.get_vertex('Clinica Lomas de Zamora'), g.get_vertex('Clinica De Niños')))
    g.add_edge(Edge(g.get_vertex('Hospital Temperley'), g.get_vertex('Hospital Malvinas Argentinas')))
   
    return g 
    
G1 = build_graph(Undirected_graph)
print(G1)



#Depth First Search:

def DFS_path(graph, start, end, path):
    path.append(start)
    # Caso base
    if start == end:
        return path

    for v in graph.get_vecinos(start): 
        if v not in path:
         new_path = DFS_path(graph, v, end, path)                 
         if new_path is not None:
            return new_path 
            
path = DFS_path(G1, G1.get_vertex('Hospital Burzaco'), G1.get_vertex('Clinica De Niños'), [])

print("DFS Path:")
for v in path:
    print(f'"{v.get_name()}"', end=' ')

    
 
#Breadht First Search

def BFS(graph, start, end):
    path = [start]
    cola = [path]
    
    while cola:
        current_path = cola.pop(0)
        if current_path[-1] == end:
            return current_path    
       
        for next_vertex in graph.get_vecinos(current_path[-1]):    
            new_path = current_path + [next_vertex]
            cola.append(new_path)
    
path = BFS(G1, G1.get_vertex('Hospital Burzaco'), G1.get_vertex('Clinica De Niños'))

print() 
print('BFS Path:')
for v in path:
    print(f'{v.get_name()}', end='->')


# Calcula y muestra el tiempo de ejecución
print()
inicio = datetime.datetime.now()
fin = datetime.datetime.now()
tiempo_ejecucion = fin - inicio
print(f"\nTiempo de ejecución: {tiempo_ejecucion}")
