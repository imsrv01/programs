from graph_new import *
from queue import *

def bfs(graph, id):
    queue = Queue()
    visited = set()

    vertex = graph.all_vertices[id]
    queue.enqueue(vertex)

    while queue.isEmpty() == False:
        current = queue.dequeue()
        if current not in visited:
            visited.add(current)
            print(current.id)

        for adjacent in current.get_adjacent_vertices():
            if adjacent not in visited:
                queue.enqueue(adjacent)



if __name__ == '__main__':
    g = Graph(False)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'D')
    g.add_edge('C', 'F')
    g.add_edge('D', 'F')

    bfs(g,'A')
