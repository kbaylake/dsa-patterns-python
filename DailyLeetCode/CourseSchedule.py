#207. Course Schedule
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
        def search(dc):
            queue=deque()
            queue.append(prerequisites[0][1])
            visited=[]
            for i in range(len(queue)):
                curr=queue.popleft()
                
        return search(dc)