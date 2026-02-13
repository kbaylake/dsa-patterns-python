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
                return maxi-mini
            mini=min(mini,root.val)
            maxi=max(maxi,root.val)
            left=getMax(root.left,mini,maxi)
            right=getMax(root.right,mini,maxi)
            return max(left,right)   
        return getMax(root,root.val,root.val)