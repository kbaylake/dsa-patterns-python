# Date: 04-02-2026
#98.Validate BST
import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True # An empty tree can be a BST
        def backtrack(parent,isTrue,min,max):
            if not parent:
                return isTrue
            val=parent.val
            if val>min and val<max:
                left=backtrack(parent.left,True,min,val)
                right=backtrack(parent.right,True,val,max)
                return left and right 
            else:
                return False
        return backtrack(root,False,-math.inf,math.inf) 