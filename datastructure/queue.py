'''
Appends and pops from the end of list are fast, doing inserts or pops from the
beginning of a list is slow (because all of the other elements have to be shifted by one).
Use collections.deque (Double Ended Queue)
'''
from collections import deque
class Queue:
    def __init__(self, items=[]):
        self.items = deque(items)
        #self.items = items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.popleft()
        #return self.items.pop(0)

if __name__ == '__main__':
    q = Queue()
    print(q.size())
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue(7)
    q.enqueue(9)

    print(q.items)

    print(q.dequeue())
    print(q.items)
