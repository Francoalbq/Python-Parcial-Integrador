#Ordenamiento Topológico (Unidad 9):
#Utiliza ordenamiento topológico para modelar la secuencia de pasos 
#necesarios para diagnosticar una enfermedad en base a los síntomas. 
#Algunos pasos requieren la realización de pruebas antes de avanzar a la 
#siguiente fase del diagnóstico.

class Directed_Graph:    # Grafo dirigido
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
        self.graph_dict[v1].append(v2)  # Agregar el vértice v2 a la lista de v1
    
    def get_vecinos(self, vertex):
        return self.graph_dict[vertex]
    
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')
        return None
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + ' ----> ' + v2.get_name() + '\n'
        return all_edges

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.get_name() + ' ---> ' + self.v2.get_name()

class Vertex:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name

def build_graph(graph):
    g = graph()
    for v in ('Sintomas', 'Examen fisico', 'Examen de Diagnostico', 'Cultivos de Esputo', 'Factores de Riesgo', 'Tratamiento'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('Sintomas'), g.get_vertex('Examen de Diagnostico')))
    g.add_edge(Edge(g.get_vertex('Sintomas'), g.get_vertex('Examen fisico')))
    g.add_edge(Edge(g.get_vertex('Examen fisico'), g.get_vertex('Examen de Diagnostico')))
    g.add_edge(Edge(g.get_vertex('Examen fisico'), g.get_vertex('Cultivos de Esputo')))
    g.add_edge(Edge(g.get_vertex('Cultivos de Esputo'), g.get_vertex('Examen de Diagnostico')))
    g.add_edge(Edge(g.get_vertex('Examen de Diagnostico'), g.get_vertex('Factores de Riesgo')))
    g.add_edge(Edge(g.get_vertex('Factores de Riesgo'), g.get_vertex('Cultivos de Esputo')))
    g.add_edge(Edge(g.get_vertex('Factores de Riesgo'), g.get_vertex('Tratamiento')))
    g.add_edge(Edge(g.get_vertex('Cultivos de Esputo'), g.get_vertex('Tratamiento')))
    
    return g

def ordenamiento_topologico(grafo):
    visitados = set()  # Un conjunto para marcar los nodos visitados
    camino = []  # Lista que almacenará el orden topológico

    # Función auxiliar DFS para explorar los nodos
    def dfs(nodo, camino):
        visitados.add(nodo)  
        for vertice in grafo.get_vecinos(nodo):  
            if vertice not in visitados:  
                dfs(vertice, camino)  
        
        camino.append(nodo)  

    # Iteramos sobre todos los nodos del grafo
    for vertice in grafo.graph_dict:
        if vertice not in visitados:  
            dfs(vertice, camino)  

    return camino[::-1]  


# Construcción del grafo
G1 = build_graph(Directed_Graph)

# Obtención del orden topológico
order = ordenamiento_topologico(G1)

# Imprimir el orden topológico
print("Orden Topológico:")
for v in order:
    print(f'{v.get_name()}', end=' -> ')
