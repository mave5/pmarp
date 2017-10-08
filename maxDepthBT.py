

'''

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

'''

#%%


# Python program to find the maximum depth of tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def maxDepth(node):

    if node is None:
        return 0
    
    return max(maxDepth(node.left),maxDepth(node.right))+1 


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print "Height of tree is %d" %(maxDepth(root))

# Time Complexity: O(n), n number of nodes 
   