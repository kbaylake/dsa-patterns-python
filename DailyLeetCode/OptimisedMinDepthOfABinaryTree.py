# Date: 13-02-2026
#111. Minimum Depth of a Binary Tree
# Definition for a binary tree node.\
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if not root:
                return 0
            if not root.left:
                return getDepth(root.right)+1
            elif not root.right:
                return getDepth(root.left)+1
            return(1 + min(getDepth(root.left), getDepth(root.right)))
        return getDepth(root)