
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self, items=[]):
        self.root = None
        if items == []:
            self.root = None
        else:
            items.sort()
            self.root = createBST(self.root, items, 0, len(items))
        
    
#Height of tree = MAX (Height of left tree, Height of right tree) + 1
#Height of empty node is -1
def height(root):
    if root == None:
        return -1
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    if lheight > rheight:
        max = lheight
    else:
        max = rheight
    
    return (max + 1)

# Minimum Node pointer       
def findMin(root):
    if root == None:
        return False
    while(root.left != None):
        root = root.left
    return root

# Maximum Node pointer
def findMax(root):
    if root == None:
        return False

    while(root.right != None):
        root = root.right
    return root   

# find a node - return true/false
def search(root, data):
    if root == None:
        return False
    if root.data == data:
        return True
    elif data > root.data:
        return search(root.right, data)
    else:
        return search(root.left, data)

# Add element
def insert(root,data):
    if root == None:
        root = Node(data)
        return root
    if data > root.data:
        if root.right == None:
            root.right = Node(data)
        else:
            insert(root.right, data)
    else:
        if root.left == None:
            root.left = Node(data)
        else:
            insert(root.left, data)
    return root

# Remove element            
def remove(root, data):
    if root == None:
        return root
    if data > root.data:
        root.right = remove(root.right, data)
    else:
        if data < root.data:
            root.left = remove(root.left, data)
        else:
            if root.left == None and root.right == None:
                root = None
            else:
                if root.left == None:
                     root = root.right
                else:
                    if root.right == None:
                        root = root.left
                    else:
                        minref = findMin(root.right)
                        print("found min - ", minref.data)
                        root.data = minref.data
                        root.right = remove(root.right, minref.data)
    return root

def BFT(root):
    q = deque([])
    q.append(root)
    while (len(q) != 0):
        temp = q.popleft()
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)
        print(temp.data, end=" ")

      

def createBST(root, list1, low, high):
    if low < high:
        pivot = (low + high)//2 
        data = list1[pivot]
        
        root = Node(data)
        
        root.left= createBST(root.left,list1, low , pivot)
        root.right = createBST(root.right, list1, pivot+1 , high)
        
        return root
    
root = Node(75)
root.left = Node(65)
root.left.left = Node(55)
root.left.left.left = Node(25)

root.right = Node(85)
root.right.right = Node(95)
root.right.right.right = Node(105)
#root.right.right.right.right = Node("59")


# Height
print('Height of tree is {}'.format(height(root)))

# Search
checkifpresent = 105
print("{} present ? - {}".format(checkifpresent, search(root, checkifpresent)))

# Insert
insertdata = 66
print("Inserting - ", insertdata)
root = insert(root, insertdata)
BFT(root)
print("")
root = insert(root, 44)
BFT(root)
print("")
root = insert(root, 77)
BFT(root)
print("")
root = insert(root, 2)
BFT(root)
print("")
checkifpresent = insertdata
print("{} present ? - {}".format(checkifpresent, search(root, checkifpresent)))

# remove
removedata = 105
print("Removing - ", removedata)
root = remove(root,removedata)
checkifpresent = removedata
print("{} present ? - {}".format(checkifpresent, search(root, checkifpresent)))

# BFT
#print(root.data)
BFT(root)

# Get Min and Max
print('minimum - ', findMin(root).data)
print('maximum - ', findMax(root).data)


# BST
list1=[1,8,5,2,9,17,12]
list1.sort()
temp = None
temp1 = createBST(temp, list1, 0, len(list1))
print('')
#print(temp1.data)
BFT(temp1)

print('')
bst = BSTree(list1)
BFT(bst.root)
