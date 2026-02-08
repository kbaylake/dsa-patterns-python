# Date: 08-02-2026
# #133. Clone Graph
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        def bfs(node):
            queue=deque()
            queue.append(node)
            visited={}
            while queue:
                for i in range(len(queue)):
                    curr=queue[0]
                    queue.popleft()
                    neigh=[]
                    val=curr.val
                    newNode=Node()
                    newNode.val=val
                    visited[curr]=newNode
                    for v in curr.neighbors:
                        if v in visited:
                            vNeigh=visited[v].neighbors
                            vNeigh.append(newNode)
                            visited[v].neighbors=vNeigh
                            neigh.append(v)
                        else:
                            queue.append(v)
                    newNode.neighbors=neigh
            return visited[node]
        return bfs(node)