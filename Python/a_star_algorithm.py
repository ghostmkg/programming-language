from heapq import heappop, heappush

# A* Algorithm implementation
def a_star(graph, start, goal, h):
    # Priority queue to store (f(n), node, g(n), path)
    open_list = []
    heappush(open_list, (h(start), start, 0, [start]))  # Push start node with heuristic h(start)
    
    # Closed set to keep track of visited nodes
    closed_set = set()

    while open_list:
        # Get the node with the lowest f(n)
        f, current, g, path = heappop(open_list)

        # If goal is reached, return the path and total cost
        if current == goal:
            return path, g

        # Add current node to the closed set
        closed_set.add(current)

        # Explore neighbors of current node
        for neighbor, cost in graph[current]:
            if neighbor in closed_set:
                continue

            # Calculate g(n) for neighbor
            g_neighbor = g + cost

            # Push neighbor with its calculated f(n) = g(n) + h(n)
            heappush(open_list, (g_neighbor + h(neighbor), neighbor, g_neighbor, path + [neighbor]))

    return None  # No path found

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 1)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('G', 2)],
    'F': [('C', 1), ('G', 3)],
    'G': [('E', 2), ('F', 3)]
}

# Example heuristic function (for simplicity, assume 0 for goal node)
def heuristic(node):
    H = {'A': 7, 'B': 6, 'C': 2, 'D': 4, 'E': 3, 'F': 1, 'G': 0}
    return H.get(node, float('inf'))

# Run A* algorithm to find the shortest path from 'A' to 'G'
start_node = 'A'
goal_node = 'G'
path, cost = a_star(graph, start_node, goal_node, heuristic)

print(f"Shortest path: {path}")
print(f"Total cost: {cost}")
