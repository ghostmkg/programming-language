import heapq

def dijkstra(n, graph, src):
    """
    n     -> number of vertices
    graph -> adjacency list: {u: [(v, weight), (v2, weight2), ...]}
    src   -> source vertex
    """
    # Step 1: Initialize distances to infinity
    dist = [float('inf')] * n
    dist[src] = 0

    # Step 2: Min-heap to get vertex with smallest distance
    pq = [(0, src)]  # (distance, node)

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if curr_dist > dist[u]:
            continue

        # Step 3: Explore neighbors
        for v, weight in graph.get(u, []):
            new_dist = curr_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
