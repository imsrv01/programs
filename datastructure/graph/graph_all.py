import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self.min_heap=[]
        self.tasks={}
        self.counter=0
    
    def add_task(self, task, priority):
        if task in self.tasks:
            raise KeyError('Key {} already present in the heap'.format(task))
        item = [priority, self.counter, task]
        heapq.heappush(self.min_heap, item)
        self.tasks[task] = item
        self.counter += 1
    
    def remove_task(self, task):
        if task not in self.tasks:
            raise KeyError('Task {} not present in heap'.format(task))
        item = self.tasks[task]
        self.tasks.pop(task)
        item[-1] = '<Removed>'
        
    def update_task_priority(self, task, priority):
        if task in self.tasks:
            self.remove_task(task)
        self.add_task(task, priority)
    
    def pop_task(self):
        while self.min_heap:
            priority, order, task = heapq.heappop(self.min_heap)
            if task != '<Removed>':
                self.tasks.pop(task)
                return (priority, order, task)
        raise KeyError('POP operation cannot be performed ..Empty priority queue. ')
    
    def is_empty(self):
        return len(self.tasks) == 0
        
    def contains_task(self, task):
        if task in self.tasks:
            return True
        else:
            return False
            
    def get_task_priority(self, task):
        if task in self.tasks:
            return (self.tasks[task])[0]
        raise ValueError("task does not exist")

        
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
    def __init__(self, is_directed=False):
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
            
class DisjointSet:
    def __init__(self):
        self.map = {}
    
    class Node:
        def __init__(self,data, rank=0, parent=None):
            self.data = data
            self.rank = rank
            self.parent = parent
            
    def makeSet(self, data):
        node = self.Node(data)
        node.parent = node
        self.map[data] = node
    
    def union(self, data1, data2):
        parent1 = self.find(data1)
        parent2 = self.find(data2)
        
        if parent1 == parent2:
            return
        
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        
    
    # Find the set in which input node/data is present, return parent pointer.. Also perform path compression by pointing all chils to root node..
    def find(self, data):
        node = self.map[data]
        if node.parent == node:
            return node.parent
        node.parent = self.find(node.parent.data)
        return node.parent          

def prims_mst(graph):
    print('Running Prims algorithm for finding minimum spanning tree...')
    pq = PriorityQueue()
    vertex_to_edge_map = {}
    result_edge_list = []
    
    # Read all vertices from graph and add to priority queue with priority infinity
    for vertex in graph.all_vertices.values():
        pq.add_task(vertex, sys.maxsize)

    # Fetch any vertex
    start_vertex = next(iter(graph.all_vertices.values()))
    
    # set its priority to zero
    pq.update_task_priority(start_vertex, 0)
    
    # While q is not Empty
    while pq.is_empty() == False:
        
    # POP the item with lease priority queue
        priority, index, currentVertex = pq.pop_task()
        print('currentVertex - ', currentVertex.id)
        
    #check if vertex is present in vertex-edge map.. if present them add the edge in result list..
        if currentVertex in vertex_to_edge_map:
            result_edge_list.append(vertex_to_edge_map[currentVertex])
            
    # Get the vertex edges
    # for each edge , get the weight and compare with vertex priority, if lesser update the priority in queue..
        for edge in currentVertex.edges:
            if edge.vertex1 == currentVertex:
                adjacentVertex = edge.vertex2
            else:
                adjacentVertex = edge.vertex1
            print('AdjacentVertex - ', adjacentVertex.id)   
            print('Edge Weight - ', edge.weight)
            print('adjacent vertex present in pq - ', pq.contains_task(adjacentVertex))
            if pq.contains_task(adjacentVertex):
                print('Priority - ', pq.get_task_priority(adjacentVertex)) 
            
            
            # Add the vertex and associated edge to a map..This will be used to get the edges that will create the resulting MST
            if pq.contains_task(adjacentVertex) and pq.get_task_priority(adjacentVertex) > edge.weight:
                pq.update_task_priority(adjacentVertex, edge.weight)
                vertex_to_edge_map[adjacentVertex] = edge
                print(edge.vertex1.id, edge.vertex2.id)
                
    return  result_edge_list       
    
def kruskals_mst(graph):
    
    ds = DisjointSet()
    result_list = []
    # sort the edges based on the weight
    edges = sorted(graph.all_edges, key=lambda edge: edge.weight)
    
    # Add each graph vertex in disjoint set. call makeset for each vertex
    for vertex in graph.all_vertices.keys():
        ds.makeSet(vertex)
    
    # for each edge in sorted list, check if its vertices belong to same set..    
    for edge in edges:
        parent1 = ds.find(edge.vertex1.id)
        parent2 = ds.find(edge.vertex2.id)
        
        # if edge vertices belong to same set, it means this edge is creating a cycle.. skip it..
        if parent1 == parent2:
            continue
        
        # else call union on edge vertices and add to same set.. Add the edge to result list..
        ds.union(parent1.data, parent2.data)
        result_list.append(edge)
    
    return result_list
    

def dijkstra_shortestpath(graph, source_vertex):
    print('Running dijkstra algorithm for finding single source shortest path....')
    pq = PriorityQueue()
    vertex_distance_map = {}
    
    # Read all vertices from graph and add to priority queue with priority infinity
    for vertex in graph.all_vertices.values():
        pq.add_task(vertex, sys.maxsize)

    # set its priority to zero
    pq.update_task_priority(source_vertex, 0)
    
    # While q is not Empty
    while pq.is_empty() == False:
        
    # POP the item with lease priority queue
        priority, index, currentVertex = pq.pop_task()
        
        # Update distance in map..
        vertex_distance_map[currentVertex.id] = priority
        
    # Get the vertex edges
    # for each edge , get the weight and compare with vertex priority, if lesser update the priority in queue..
        for edge in currentVertex.edges:
            if edge.vertex1 == currentVertex:
                adjacentVertex = edge.vertex2
            else:
                adjacentVertex = edge.vertex1
            
            # if vertext not present in PQ, skip
            if pq.contains_task(adjacentVertex) == False:
                continue
            
            # calculate new distance of adjancent vertex - D(source) + weight
            distance = vertex_distance_map[currentVertex.id] + edge.weight
            
            # Compare the adjacent vertex distance with new distance, if greater than update with new distance
            if pq.get_task_priority(adjacentVertex) > distance:
                pq.update_task_priority(adjacentVertex, distance)
                
                
    return  vertex_distance_map  
