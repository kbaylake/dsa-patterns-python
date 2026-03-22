#79. Word Search
#22-03-2026
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neigh=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(boarad,i,j,level):
            if level==len(word):
                return True
            curr=board[i][j]
            board[i][j]='#'
            neighs=[]
            for v in neigh:
                newi=i+v[0]
                newj=j+v[1]
                if 0<=newi<len(board) and 0<=newj<len(board[0]) and 0<=level<len(word):
                            if board[newi][newj]==word[level]:
                                neighs.append([newi,newj])
            for n in neighs:
                val=dfs(board,n[0],n[1],level+1)
                if val==True:
                    return True
            board[i][j]=curr
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    curr=dfs(board,i,j,1)
                    if curr==True:
                        return True
        return False
