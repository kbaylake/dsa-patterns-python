# Date: 15-01-2026
#1448-count-good-nodes-in-binary-tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,curr):
            if not root:
                return 0
            left=dfs(root.left,max(curr,root.val))
            right=dfs(root.right,max(curr,root.val))
            count=left+right
            if root.val>=curr:
                count+=1 
            return count 
        return dfs(root,float('-inf'))