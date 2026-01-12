# Date: 12-01-2026
# Leet Code 94. Binary Tree In Order Trevarsal
# Recursively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        parent=root
        if not root:
            return []
        def search(parent):
            if not parent:
                return
            left=parent.left
            search(left)
            ans.append(parent.val)
            right=parent.right
            search(right)
        search(root)   
        return ans   
# Iteratively
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[]
        parent=root
        if not root:
            return []
        while True:
            while parent:
                stack.append(parent)
                parent=parent.left
            if len(stack)==0:
                break
            parent=stack[-1]
            ans.append(parent.val)
            stack.pop()
            parent=parent.right
        return ans