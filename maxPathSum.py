'''

Given a binary tree, find the maximum path sum.

A path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

sum=6


there are four values/paths to check each time
- root only
- left+root
- right+root
- left+root+right

'''
#%%


# A Binary Tree Node
class Node:
     
    # Contructor to create a new node
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
 

def findMaxHelper(node):
    
    if node is None:
        return 0
    
    # max of left/right path
    leftMax=findMaxHelper(node.left)
    rightMax=findMaxHelper(node.right)
    
    
    # max of single path: either left or right
    maxSingle=max(max(leftMax,rightMax)+node.value,node.value)
    
    # max from node
    maxTop=max(maxSingle,leftMax+rightMax+node.value)
    
    # static variable
    findMaxHelper.result=max(findMaxHelper.result,maxTop)
    
    return maxSingle

def findMaxSum(root):
    
    findMaxHelper.result=float('-inf')
    
    findMaxHelper(root)
    return findMaxHelper.result

# Driver program 
root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
print "Max path sum is " ,findMaxSum(root);