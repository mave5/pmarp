'''

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally 
identical and the nodes have the same value.
'''

#%%


# Python program to determine if two trees are identical
 
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        

def issameTree(node1,node2):
    
    if node1 is None and node2 is None:
        return True
    
    if node1.value == node2.value:
        return issameTree(node1.left,node2.left) and issameTree(node1.right,node2.right)
    return False
    
 
# Driver program to test identicalTress function
root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
 
if issameTree(root1, root2):
    print "Both trees are identical"
else:
    print "Trees are not identical"
    
    
'''
Complexity of the identicalTree() will be according to the tree with lesser 
number of nodes. Let number of nodes in two trees be m and n then complexity
 of sameTree() is O(m) where m < n.
'''    
 