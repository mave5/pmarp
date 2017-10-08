'''

Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure
 and node values with a subtree of s. A subtree of s is a 
 tree consists of a node in s and all of this node's descendants. 
 The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''
#%%

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isMatch(s,t):
   
    if not (s and t):
        return s is t
    
    return (s.val==t.val and isMatch(s.left,t.left) and isMatch(s.right,t.right))

def isSubtree(s,t):
    
    if isMatch(s,t): 
        return True
    
    if not s:
        return False
    
    return isSubtree(s.left,t) or isSubtree(s.right,t)


n1=TreeNode(3)
n1L=TreeNode(9)
n1R=TreeNode(20)
n1.left=n1L
n1.right=n1R

print isSubtree(None,n1)
