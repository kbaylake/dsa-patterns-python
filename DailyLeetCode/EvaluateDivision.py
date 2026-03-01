#01-03-2026
#399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        nodes=dict.fromkeys(val for row in equations for val in row)
        cnt=0
        for i in nodes:
            nodes[i]=cnt
            cnt+=1
        adj=[[-1 if i!=j else 1 for i in range(len(nodes))] for j in range(len(nodes))]
        start=0
        for equation in equations:
            x=nodes[equation[0]]
            y=nodes[equation[1]]
            adj[x][y]=values[start]
            adj[y][x]=1/values[start]
            start+=1
        def dfs(source,sink,visited):
            if source==sink:
                return 1
            if adj[source][sink]!=-1:
                return adj[source][sink]
            visited.append(source)
            neigh=[i for i in range(len(adj[source])) if i not in visited and adj[source][i]!=-1]
            if not neigh:
                return -1
            for v in neigh:
                nv=dfs(v,sink,visited)
                if nv==-1:
                    continue
                return adj[source][v]*nv
            return -1
        ans = [
            dfs(nodes[query[0]], nodes[query[1]], [])
            if query[0] in nodes and query[1] in nodes
            else -1 
            for query in queries
        ]
        return ans
