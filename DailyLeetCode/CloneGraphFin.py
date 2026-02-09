# Date: 08-02-2026
# #133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
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
                curr=queue.popleft()
                if curr not in visited:
                    newNode=Node(curr.val)
                    visited[curr]=newNode
                    neigh=[]
                else:
                    newNode=visited[curr]
                    neigh=newNode.neighbors
                for v in curr.neighbors:
                    if v not in visited:
                        newNeigh=Node(v.val,[newNode])
                        neigh.append(newNeigh)
                        visited[v]=newNeigh
                        queue.append(v)
                    else:
                        newNeighs=visited[v]
                        if newNode not in newNeighs.neighbors:
                            newNeighs.neighbors.append(newNode)
                            neigh.append(newNeighs)
                newNode.neighbors=neigh
            return visited[node]
        return bfs(node)