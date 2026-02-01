# Date: 01-02-2026
#130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfsEdge(i,j):
            queue=[]
            queue.append([i,j])
            neigh=[[0,1],[1,0],[-1,0],[0,-1]]
            board[i][j]='#'
            while queue:
                size=len(queue)
                for num in range(size):
                    i,j=queue[0]
                    queue.pop(0)
                    for v in neigh:
                        newi=i+v[0]
                        newj=j+v[1]
                        if 0<=newi<len(board) and 0<=newj<len(board[0]) and board[newi][newj]=='O':
                            board[newi][newj]='#'
                            queue.append([newi,newj])
            return
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1) and board[i][j]=='O':
                    #print([i,j],board[i][j])
                    bfsEdge(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='#':
                    board[i][j]='O'
              
        return 