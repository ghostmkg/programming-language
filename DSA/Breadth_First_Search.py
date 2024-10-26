# Breadth_First_Search.py

from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    
    while queue:
        vertex = queue.popleft()  # Dequeue the front node
        if vertex not in visited:
            visited.add(vertex)  # Mark it as visited
            print(vertex, end=' ')  # Process the node (here we just print it)
            # Enqueue all unvisited neighbors
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS starting from vertex 'A':")
    bfs(graph, 'A')
