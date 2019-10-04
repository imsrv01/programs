
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
    
root = Node("25")
root.left = Node("45")
root.right = Node("55")
root.right.right = Node("75")
root.right.right.right = Node("81")
#root.right.right.right.right = Node("59")
root.left.left = Node("17")
root.left.left.left = Node("59")

print('Height of tree is {}'.format(height(root)))
