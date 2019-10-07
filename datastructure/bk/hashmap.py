
class HashMap:
    def __init__(self):
        self.store = [None for i in range(16)]
        self._size = 0
    
    def add(self, key, value):
        # Get hash value for key
        index = self.getHash(key)
        
        # create a node object containing key/value pair
        node = Node(key,value)
        # check if any value present at that index
        # if not initialize it with list containing the Key/value pair
        if not self.store[index]:
            
            self.store[index] = [node]
            self._size += 1
        else:
            # if present, check if key already present, if yes, update value to new value
            present=False
            listref = self.store[index]
            for node in listref:
                if node.key == key:
                    node.value = value
                    present = True
                    break
            # else append the key/value pair    
            if present == False:
                listref.append(node)
                self._size += 1
        
    
    def get(self, key):
        # Get hash key
        index = self.getHash(key)
        # check if any value present at the index, it no value, then rturn False
        if not self.store[index]:
            return False
        else:
            # if present, get the list at the index, find the key and update
            present = False
            listref = self.store[index]
            for node in listref:
                if node.key == key:
                    present = True
                    return node.value
            if present == False:
                return False
            
        # if not present, then return False
    
    def getHash(self, key):
        hashValue=0
        if isinstance(key, int) or isinstance(key, float):
            hashValue = key
        else:
            for char in key:
                hashValue = hashValue + ord(char)
        return (hashValue % len(self.store))
        
    def size(self):
        return self._size
    
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

hmObj = HashMap()
print(hmObj.store)
print(hmObj.size())
hmObj.add(100, "Neeraj")
hmObj.add(101, "Neeraj1")
print(hmObj.get(101))
hmObj.add(90000, "Neeraj2")
hmObj.add(102, "Neeraj3")
hmObj.add(101, "RUDRA")
print(hmObj.size())
print(hmObj.get(102))
print(hmObj.get(100))
print(hmObj.get(900001))
print(hmObj.get(101))
