'''
original
     4
   /   \
  2     7
 / \   / \
1   3 6   9


inverted
    4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

#%%

def invertTree(root):
    if root:
        # when we swap right and left chils, all of the sub-childs will be swapped
        # at the same time since we swap the address and not the value/key
        root.left,root.right=root.right,root.left # 
        
        # swapping sub-childs
        invertTree(root.left) 
        invertTree(root.right)
    return root    

    

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    
# Driver program to test identicalTress function
root1 = Node(1)

root1.left = Node(2)
root1.right = Node(3)

root1.left.left = Node(4)
root1.left.right = Node(5)

root1.right.left = Node(6)
root1.right.right = Node(7)
 
iroot1=invertTree(root1)
