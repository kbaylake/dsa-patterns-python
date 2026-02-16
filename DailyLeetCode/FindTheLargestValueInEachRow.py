#Date 16-02-2026
#515. Find the largest Value in each row
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(root,ans):
            queue=deque([root])
            while queue:
                level=len(queue)
                maxi=-math.inf
                for i in range(level):
                    node=queue.popleft()
                    maxi=max(maxi,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(maxi)
            return ans
        return bfs(root,[])