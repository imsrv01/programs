
class MaxHeap:
    def __init__(self,items=[]):
        self.heap=[0]
        for i in range(len(items)):
            self.heap.append(items[i])
            self.__floatUp(len(self.heap)-1)

    def __floatUp(self, index):
        parent = index/2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __swap(self, left, right):
        self.heap[left], self.heap[right] = self.heap[right], self.heap[left]

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__heapify(1)
        elif len(self.heap) == 2:
            max = self.pop()
        else:
            max = False
        return max

    def __heapify(self, index):
        left = 2*index
        right = 2*index + 1
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.__swap(largest, index)
            self.__heapify(largest)


maxheap = MaxHeap([2,32,5,17,98,12])
print(maxheap.heap)

print('PEEK - ', maxheap.peek())

#maxheap.push(88)
#print('PUSH - ', maxheap.heap)

print('POP - ', maxheap.pop())
print(maxheap.heap)
print('POP - ', maxheap.pop())
print(maxheap.heap)
print('POP - ', maxheap.pop())
print(maxheap.heap)
print('POP - ', maxheap.pop())
