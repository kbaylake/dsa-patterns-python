# Date: 10-02-2026
#112 Path Sum 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,target):
            if not root:
                return False
            curr=target-root.val
            if not root.left and not root.right:
                return curr==0
            left=dfs(root.left,curr)
            right=dfs(root.right,curr)
            return left or right
        return dfs(root,targetSum)