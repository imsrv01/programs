from graph_new import *
from stack import *

def dfs(graph, id):
    stack = Stack()
    visited = set()

    vertex = graph.all_vertices[id]
    stack.push(vertex)

    while stack.isEmpty() == False:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            print(current.id)

        for adjacent in current.get_adjacent_vertices():
            if adjacent not in visited:
                stack.push(adjacent)



if __name__ == '__main__':
    g = Graph(False)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'D')
    g.add_edge('C', 'F')
    g.add_edge('D', 'F')

    dfs(g,'A')
