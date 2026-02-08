# Date: 08-02-2026
# #133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        def bfs(node):
            queue=[]
            queue.append(node)
            visited=[]
            adj={}
            while queue:
                for a in range(len(queue)):
                    curr=queue[0]
                    visited.append(curr)
                    queue.pop(0)
                    neigh=[]
                    for v in curr.neighbors:
                        neigh.append(v.val)
                        if v not in visited:
                            queue.append(v)  
                    adj[curr.val]=neigh
            return adj
        adj=bfs(node)
        tmp=list(adj.keys())
        tmp.sort()
        nodesList=[Node(i) for i in tmp]
        for i in adj:
            neigh=[nodesList[v-1] for v in adj[i]]
            nodesList[i-1].neighbors=neigh

        return nodesList[0]