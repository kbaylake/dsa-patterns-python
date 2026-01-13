# Date: 13-01-2026
# Leet Code 103. Binary Tree ZigZag Level Order Trevarsal
# Iteratively
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        queue=[]
        queue.append(root)
        ans.append([root.val])
        lr=1
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                curr=queue[0]
                queue.pop(0)
                if curr.left:
                    level.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    queue.append(curr.right)
            if lr==1:
                level=level[::-1]
                lr=0
            else:
                lr=1
            if level:
                ans.append(level)
        return ans