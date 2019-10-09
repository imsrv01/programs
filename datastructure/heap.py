
class MaxHeap:
    def __init__(self,items=[]):
        self.heap=[0]
        for i in range(len(items)):
            self.heap.append(items[i])
            self.__floatUp(len(self.heap)-1)

    # 2 - Place it at correct position - Float UP
    #     a. get parent
    #     b. Compare with parent, if greater than swap & floatup parent..
    #     Exit condition - if element is first element .. i,e i <= 1 , just return .. do nothing..
    def __floatUp(self, index):
        parent = index/2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __swap(self, left, right):
        self.heap[left], self.heap[right] = self.heap[right], self.heap[left]

    # Get max/min element in heap
    # -- return first element in list..
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    # Add new element -
    # 1 - Add to end of array - list append
    # 2 - Place it at correct position - Float UP
    #     a. get parent
    #     b. Compare with parent, if greater than swap & floatup parent..
    #     Exit condition - if element is first element .. i,e i <= 1 , just return .. do nothing..
    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    # Remove element- Only top element can be removed..
    # 1. If heap size > 2
    #       swap last element with first element
    #       remove last element from list
    #        heapify
    # 2. If heap size == 2
    #       remove last element
    # 3. else return False
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.__heapify(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    # Heapify - Place a given element at it correct position
    # 1. Get left and right child
    # 2. largest = index
    # 3. If left child > largest, make left child largest
    # 4. if right child > largest , make right child largest
    # 5. If left/right child is greater than index
    #     a. swap index and largest
    #     b. heapify largest
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
