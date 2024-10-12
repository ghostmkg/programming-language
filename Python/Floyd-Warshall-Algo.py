def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of vertices in a weighted graph.

    Parameters:
    graph (list of list of float): A 2D list representing the adjacency matrix
                                    of the graph. A value of float('inf') indicates
                                    no edge between vertices.

    Returns:
    list of list of float: A 2D list containing the shortest path distances
                           between all pairs of vertices.
    """
    # Number of vertices in the graph
    num_vertices = len(graph)

    # Initialize the distance matrix with the input graph
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Set the distance from each vertex to itself to 0
    for i in range(num_vertices):
        distance[i][i] = 0

    # Set the initial distances based on the graph's edges
    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] != float('inf'):
                distance[u][v] = graph[u][v]

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Example usage
if __name__ == "__main__":
    # Create a graph represented as an adjacency matrix
    # For example, the graph below has 4 vertices and the weights of the edges:
    #     0     1     2     3
    # 0: [ 0,   3,   inf,   7 ]
    # 1: [ inf,  0,   1,   inf ]
    # 2: [ inf, inf,   0,   2 ]
    # 3: [ inf, inf, inf,   0 ]
    graph = [
        [0, 3, float('inf'), 7],
        [float('inf'), 0, 1, float('inf')],
        [float('inf'), float('inf'), 0, 2],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    shortest_paths = floyd_warshall(graph)

    print("Shortest path distances between every pair of vertices:")
    for row in shortest_paths:
        print(row)
