
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
    
def search(root, data):
    if root == None:
        return False
    
    if root.data == data:
        return True
    elif data > root.data:
        return search(root.right, data)
    else:
        return search(root.left, data)
        
def insert(root,data):
    if root == None:
        print("empty tree")
    
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
    
root = Node("25")
root.left = Node("15")
root.right = Node("35")
root.right.right = Node("75")
root.right.right.right = Node("81")
#root.right.right.right.right = Node("59")
root.left.left = Node("10")
root.left.left.left = Node("5")

checkifpresent = "41"
print('Height of tree is {}'.format(height(root)))
print("{} present ? - {}".format(checkifpresent, search(root, checkifpresent)))

insert(root, "66")
