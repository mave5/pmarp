'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

   3
   / \
  9  20
    /  \
   15   7


[
  [3],
  [9,20],
  [15,7]
]

'''
#%%


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderTraverse(root):
    if not root:
        return []
  
    output=[]
    level=[root]
    while level:
        output.append([node.val for node in level])
        
        temp=[]
        for node in level:
            temp.extend([node.left,node.right])
        level=[leaf for leaf in temp if leaf]
    return output
    
 

n1=TreeNode(3)
n1L=TreeNode(9)
n1R=TreeNode(20)
n1.left=n1L
n1.right=n1R

n1RL=TreeNode(15)
n1RR=TreeNode(7)
n1R.left=n1RL
n1R.right=n1RR


print levelOrderTraverse(n1)
        