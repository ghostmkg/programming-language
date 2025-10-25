def isCyclic(n, edges):
    adj = [[] for i in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited=[0]*n

    def dfs(node,parent):
        visited[node] = 1
        for i in adj[node]:
            if not visited[i]:
               if dfs(i,node) == True:
                return True

            elif i!=parent:
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False