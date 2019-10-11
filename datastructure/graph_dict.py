
class Graph:
    def __init__(self, graph={}):
        if graph:
            self.graph = graph
        else:
            self.graph = {}
        
    def vertices(self):
        return list(self.graph)
    
    def edges(self):
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        
    def __generate_edges(self):
        edges=[]
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {vertex,neighbour} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __str__(self):
        res = "vertices: "
        for k in self.graph:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res            

if __name__ == "__main__":
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
            }
    graph = Graph(g)
    print('Vertices - ', graph.vertices())
    print('Edges - ', graph.edges())
    print('Add vertex - ')
    graph.add_vertex('z')
    print('Vertices - ', graph.vertices())
    graph.add_edge('a', 'z')
    print('Edges - ', graph.edges())
    print(graph)
    
    
