import heapq
from collections import defaultdict

def prim_mst(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, parent)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if parent is not None:
            mst.append((parent, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst

# Example graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst = prim_mst(graph, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")