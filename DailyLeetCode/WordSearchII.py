# Date: 05-02-2026
#212. Word Search II
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        neigh=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,nextIndex,sel):
            if nextIndex==len(word):
                return ''.join(sel[:])
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
                neighbor_char = board[child[0]][child[1]]
                print(neighbor_char)
                val=dfs(child[0],child[1],nextIndex+1,sel+[neighbor_char])
                board[i][j]=tmp
                if val:
                    return val
        ###########################
        def helper(word):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==word[0]:
                        val=dfs(i,j,1,[word[0]])
                        if val:
                            return val
        ans=[]
        for word in words:
            sol=helper(word)
            if sol:
                ans.append(sol)
        return ans  