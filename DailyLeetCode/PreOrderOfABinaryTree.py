# Date: 12-01-2026
# Leet Code 144. Binary Tree Pre Order Trevarsal
# Recursively
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        parent=root
        if not root:
            return []
        def search(parent):
            if not parent:
                return
            ans.append(parent.val)
            left=parent.left
            search(left)
            right=parent.right
            search(right)
        search(root)
        return ans 
# Ieratively
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        stack=[]
        parent=root
        if not root:
            return []
        while True:
            while parent:
                ans.append(parent.val)
                stack.append(parent)
                parent=parent.left
            if len(stack)==0:
                break
            parent=stack[-1]
            stack.pop()
            parent=parent.right
        return ans