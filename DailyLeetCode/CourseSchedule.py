#207. Course Schedule
from collections import defaultdict
from collections import deque
from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        def create(prerequisites):
            dc=defaultdict(list)
            for i in prerequisites:
                dc[i[1]].append(i[0])
            return dc
        dc=create(prerequisites)
        def dfs(node,visited,completed):
            if node in completed:
                return True
            visited.append(node)
            neigh=dc[node]
            for v in neigh:
                if v in visited:
                    return False
                cycle=dfs(v,visited,completed)
                if cycle==False:
                    return False
            visited.pop()
            completed.append(node)
            return True  
        completed=[]    
        for i in range(numCourses):
            cyc=dfs(i,[],completed)
            if cyc==False:
                return False
        return True