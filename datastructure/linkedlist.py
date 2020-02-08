
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNodeFront(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node 
        
    def addNodeAfter(self,prev_node,data):
        if prev_node == None:
            print('prev_node not pointing to any node')
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node
    
    def addNodeEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        
    def printlist(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
    
    def reverse(self):
        curr = self.head
        previous = None
        next = None
        while curr != None:
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next
        self.head = previous
    
    def deleteNode(self, data):
        if self.head == None:
            print('List empty, node not present')
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            curr = self.head.next
            previous = self.head
            while curr != None:
                if curr.data == data:
                    previous.next = curr.next
                    return
                else:
                    previous = curr
                    curr = curr.next
            
    
if __name__ == '__main__':
    list1 = LinkedList()
    list1.addNodeFront(25)
    list1.addNodeFront(30)
    list1.addNodeFront(35)
    
    print('current list: ')
    list1.printlist()
    
    list1.addNodeAfter(list1.head, 45)
    print('\nNew list: ')
    list1.printlist()
    
    list1.addNodeEnd(90)
    print('\nNew list: ')
    list1.printlist()
    
    print('\nreverse list: ')
    list1.reverse()
    list1.printlist()
    
    print('\nDelete Node')
    list1.deleteNode(35)
    list1.printlist()
