import sys
import heapq

class Vertex:
    def __init__(self, vertex):
        self.id = vertex
        self.adjacent = {}
        self.distance=sys.maxsize
        self.visited= False
        self.previous = None
    
    def __equal__(self, other):
        return self.distance == other.distance
        
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
            node = Vertex(vertex)
            self.graph[vertex] = node
            
    def add_edge(self, u, v, cost=0):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        
        self.graph[u].adjacent[self.graph[v]] = cost
        self.graph[v].adjacent[self.graph[u]] = cost
        
    def __generate_edges(self):
        edges=[]
        for vertex in self.graph:
            for neighbour in self.graph[vertex].adjacent.keys():
                if {vertex,neighbour.id} not in edges:
                    edges.append({vertex, neighbour.id})
        return edges

def dijkstra(g, start_vertex):
    unvisited_queue=[]
    g.graph[start_vertex].distance = 0
    for vertex,node in g.graph.items():
        #print(vertex,node.distance)
        unvisited_queue.append([node, node.distance])
    unvisited_queue = sorted(unvisited_queue, key=lambda vertex:vertex[1])
    
    #print(unvisited_queue)
    while len(unvisited_queue) > 1:
        #print(unvisited_queue.pop(0))
        uv = unvisited_queue.pop(0)
        current = uv[0]
        current.visited = True
        
        for adjacent in current.adjacent:
            if adjacent.visited:
                continue
            new_distance = current.distance + current.adjacent[adjacent]
            #print('new distance - ', new_distance)
            
            if new_distance < adjacent.distance:
                adjacent.distance = new_distance
                adjacent.previous = current
                print('updated - ', current.id, adjacent.id, adjacent.distance)
            else:
                print('Not updated - ', current.id, adjacent.id, adjacent.distance)
        unvisited_queue=[]
        for vertex,node in g.graph.items():
            if node.visited == False:
                unvisited_queue.append([node, node.distance])
        unvisited_queue = sorted(unvisited_queue, key=lambda vertex:vertex[1])    

if __name__ == "__main__":
    
    g = Graph()
    
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    
    print('All vertices - ', g.vertices())
    print('All Edges - ', g.edges())
    
    dijkstra(g, 'a')
    
