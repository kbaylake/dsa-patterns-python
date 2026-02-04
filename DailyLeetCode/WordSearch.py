# Date: 04-02-2026
#79. Word Search
#SubOptimal Backtracking using a visited list
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neigh=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,nextIndex,visited):
            if nextIndex==len(word):
                return True
            visited.append([i,j])
            children=[]
            for v in neigh:
                newi=i+v[0]
                newj=j+v[1]
                if 0<=newi<len(board) and 0<=newj<len(board[0]) and 0<=nextIndex<len(word):
                            if board[newi][newj]==word[nextIndex] and ([newi,newj] not in visited):
                                children.append([newi,newj])
            for child in children:
                val=dfs(child[0],child[1],nextIndex+1,visited)
                if val==True:
                    return True
            visited.pop()
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    if dfs(i,j,1,[]):
                        return True
        return False
# Optimised Solution using inplace conversions
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neigh=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,nextIndex):
            if nextIndex==len(word):
                return True
            tmp=board[i][j]
            board[i][j]='#'
            children=[]
            for v in neigh:
                newi=i+v[0]
                newj=j+v[1]
                if 0<=newi<len(board) and 0<=newj<len(board[0]) and 0<=nextIndex<len(word):
                            if board[newi][newj]==word[nextIndex]:
                                children.append([newi,newj])
            for child in children:
                val=dfs(child[0],child[1],nextIndex+1)
                if val==True:
                    return True
            board[i][j]=tmp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    if dfs(i,j,1):
                        return True
        return False                      