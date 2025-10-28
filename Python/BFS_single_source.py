def bfsOfGraph(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  
    
    visited = [False] * n
    queue = [src]   
    visited[src] = True
    bfs_result = []
    
    while queue:
        node = queue.pop(0)   
        bfs_result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  
    return bfs_result


# Example usage:
n = 5
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
src = 0
print(bfsOfGraph(n, edges, src))  # Output: [0, 1, 2, 3, 4]
# BFS traversal from a single source node in an undirected graph
# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) for the visited array and the queue