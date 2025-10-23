from collections import defaultdict, deque

def kahn_topological_sort(n, edges):
    """
    n     -> number of vertices (0 to n-1)
    edges -> list of directed edges (u -> v)
    """
    
    # Step 1: Build graph and compute in-degree
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Step 2: Initialize queue with all nodes having in-degree 0
    queue = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []

    # Step 3: Process nodes in queue
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # Decrease in-degree of neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycles
    if len(topo_order) != n:
        print("Graph contains a cycle, topological sort not possible.")
        return []

    return topo_order
