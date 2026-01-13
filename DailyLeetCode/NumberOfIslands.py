# Date: 13-01-2026
# 200. Number of Islands 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            queue=[]
            grid[i][j]='0'
            queue.append([i,j])
            neigh=[[0,1],[1,0],[-1,0],[0,-1]] 
            while queue:
                size=len(queue)
                for num in range(size):
                    i,j=queue[0]
                    queue.pop(0)
                    for v in neigh:
                        newi=i+v[0]
                        newj=j+v[1]
                        if 0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]=='1':
                            grid[newi][newj]='0'
                            queue.append([newi,newj])
            return
        op=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    op+=1
                    bfs(i,j)
        return op