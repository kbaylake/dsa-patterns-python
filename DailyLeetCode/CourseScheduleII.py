#08-03-2026
#Course Schedule II
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        completed = set()
        order = []
        def dfs(node):
            if node in visiting:
                return False
            if node in completed:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            completed.add(node)
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order[::-1]