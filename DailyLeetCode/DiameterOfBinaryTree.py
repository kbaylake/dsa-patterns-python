#Date: 13-02-2026
#Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def inorder(root,curr):
            if not root:
                return curr+1
            if not root.right:
                return inorder(root.left,curr)
            elif not root.left:
                return inorder(root.right,curr)
            return max(inorder(root.left,curr)+inorder(root.right,curr),curr)
        return inorder(root,0)