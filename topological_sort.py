from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Dictionary containing adjacency List
        self.V = vertices               # Number of vertices

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to perform topological sort using Kahn's Algorithm
    def topological_sort(self):
        # Step 1: Calculate in-degree of each vertex
        in_degree = [0] * self.V
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Step 2: Create a queue and enqueue all vertices with in-degree 0
        queue = deque()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Step 3: Initialize count of visited vertices and the result list
        visited_count = 0
        top_order = []

        # Step 4: Process nodes in the queue
        while queue:
            u = queue.popleft()
            top_order.append(u)

            # Iterate through all adjacent nodes of dequeued node u and decrease their in-degree by 1
            for v in self.graph[u]:
                in_degree[v] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[v] == 0:
                    queue.append(v)

            visited_count += 1

        # Check if there was a cycle (visited_count != number of vertices indicates a cycle)
        if visited_count != self.V:
            print("There exists a cycle in the graph.")
        else:
            print("Topological Sort:", top_order)

# Example usage:
if __name__ == "__main__":
    g = Graph(6)  # Number of vertices in the graph
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Sorting of the graph:")
    g.topological_sort()
