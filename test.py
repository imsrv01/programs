class HashMap:
    def __init__(self):
        self.map = [None for _ in range(16)]

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, node):
        return self.key == node.key


n = Node("a", "b")
n1 = Node("c", "d")
print(n.key)
print(n1.key)
print(n.key == n1.key)
#print(hash(n) == hash(n1))
print(hash(n.key ))
print(hash(n1.key))
print(n == n1)

hm = HashMap()
print(hm.map)
