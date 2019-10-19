

class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent_vertices = []
        self.edges = []

    def add_adjacent_vertex(self, edges, vertex):
        self.edges.append(edges)
        self.adjacent_vertices.append(vertex)

    def get_adjacent_vertices(self):
        adjacent_vertices=[]
        for vertex in self.adjacent_vertices:
            adjacent_vertices.append(vertex)
        return adjacent_vertices

    def get_edges(self):
        edges=[]
        for edge in self.edges:
            edges.append((edge.vertex1.id, edge.vertex2.id))
        return edges

class Edge:
    def __init__(self, vertex1, vertex2, is_directed, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.is_directed = is_directed
        self.weight = weight

class Graph:
    def __init__(self, is_directed):
        self.all_vertices={}
        self.all_edges= []
        self.is_directed = is_directed

    def vertices(self):
        return self.all_vertices

    def edges(self):
        edges=[]
        for edge in self.all_edges:
            edges.append((edge.vertex1.id, edge.vertex2.id))
        return edges

    def add_edge(self, id1, id2, weight=0):
        # Add vertex if not present
        if id1 not in self.all_vertices:
            vertex1 = Vertex(id1)
            self.all_vertices[id1] = vertex1
        else:
            vertex1 = self.all_vertices[id1]

        if id2 not in self.all_vertices:
            vertex2 = Vertex(id2)
            self.all_vertices[id2] = vertex2
        else:
            vertex2 = self.all_vertices[id2]

        # Add an edge, update grah edges and update vertex adjacent
        edge = Edge(vertex1, vertex2, self.is_directed, weight)
        self.all_edges.append(edge)
        vertex1.add_adjacent_vertex(edge, vertex2)
        if self.is_directed == False:
            vertex2.add_adjacent_vertex(edge, vertex1)

    def add_vertex(self):
        pass

if __name__ == '__main__':
    g = Graph(False)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'D')
    g.add_edge('C', 'F')
    g.add_edge('D', 'F')

    print('All Vertices - ', g.vertices().keys())
    print('All Edges - ', g.edges())

    for id,vertex in g.vertices().items():
        print('Vertex - ' + id)
        print('--> Adjacent Vertices: ', map(lambda x : x.id , vertex.get_adjacent_vertices()))
        print('--> Edges: ',vertex.get_edges())
