
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
    
    # Simple Path - Path with no repeated vertices
    # Path - A path in an undirected graph is a sequence of vertices P = ( v1, v2, ..., vn ) 
    #       such that vi is adjacent to v{i+1} for 1 ≤ i < n. Such a path P is called a path of length n from v1 to vn.
    def find_path(self, start_vertex, end_vertex, path=None):
        
        graph = self.graph
        if path == None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        
        for vertex in graph[start_vertex]:
            if vertex not in path:
                final_path = self.find_path(vertex, end_vertex, path)
                if final_path:
                    return final_path
        return None
    
    def find_path_all(self, start_vertex, end_vertex, path=None):
        
        graph = self.graph
        if path == None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths=[]
        for vertex in graph[start_vertex]:
            if vertex not in path:
                final_path = self.find_path_all(vertex, end_vertex, path)
                
                for p in final_path:
                    paths.append(p)
        return paths
        
if __name__ == "__main__":
    g = { "a" : ["d",'f'],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c",'f'],
          "e" : ["c"],
          "f" : ['d','a']
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
    print('Find path - A to B ', graph.find_path('a', 'b'))
    print('Find path - A to F ', graph.find_path('a', 'f'))
    print('Find path - C to C ', graph.find_path('c', 'c'))
    print('Find path - B to D', graph.find_path('b', 'd'))
    print('Find path all - A to B', graph.find_path_all('a', 'b'))
    
    
