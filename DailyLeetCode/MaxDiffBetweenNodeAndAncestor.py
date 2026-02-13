# Date: 13-02-2026
#1026. Maximum Difference Between Node and Ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getMax(root,mini,maxi):
            if not root:
                return mini,maxi
            mini=min(mini,root.val)
            maxi=max(maxi,root.val)
            l1,l2=getMax(root.left,mini,maxi)
            r1,r2=getMax(root.right,mini,maxi)
            left=abs(l2-l1)
            right=abs(r2-r1)
            if left>right:
                return l1,l2
            return r1,r2   
        a,b= getMax(root,math.inf,-math.inf)
        return abs(b-a)