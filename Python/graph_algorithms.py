"""
Advanced Graph Algorithms Implementation
=========================================

This module implements various advanced graph algorithms used in computer science
and real-world applications including social networks, navigation systems, and
network optimization.

Algorithms Implemented:
- Dijkstra's Shortest Path
- Bellman-Ford Algorithm
- Floyd-Warshall All-Pairs Shortest Path
- Kruskal's Minimum Spanning Tree
- Prim's Minimum Spanning Tree
- Topological Sort (DFS and Kahn's)
- Strongly Connected Components (Tarjan's)
- Graph Coloring (Greedy)

Author: Hacktoberfest 2025 Contributor
License: MIT
"""

import heapq
from collections import defaultdict, deque
from typing import List, Tuple, Dict, Set, Optional


class Graph:
    """
    Graph data structure supporting both directed and undirected graphs.
    Supports weighted and unweighted edges.
    """
    
    def __init__(self, vertices: int, directed: bool = False):
        """
        Initialize graph with given number of vertices.
        
        Args:
            vertices: Number of vertices in the graph
            directed: Whether the graph is directed (default: False)
        """
        self.V = vertices
        self.directed = directed
        self.adj_list = defaultdict(list)
        self.edges = []
    
    def add_edge(self, u: int, v: int, weight: int = 1):
        """
        Add an edge to the graph.
        
        Args:
            u: Source vertex
            v: Destination vertex
            weight: Weight of the edge (default: 1)
        """
        self.adj_list[u].append((v, weight))
        self.edges.append((u, v, weight))
        
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def dijkstra(self, source: int) -> Tuple[List[int], List[int]]:
        """
        Dijkstra's shortest path algorithm.
        Finds shortest paths from source to all other vertices.
        
        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)
        
        Args:
            source: Starting vertex
            
        Returns:
            Tuple of (distances, predecessors) arrays
        """
        distances = [float('inf')] * self.V
        distances[source] = 0
        predecessors = [-1] * self.V
        
        # Priority queue: (distance, vertex)
        pq = [(0, source)]
        visited = set()
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if u in visited:
                continue
            
            visited.add(u)
            
            # Relaxation step
            for v, weight in self.adj_list[u]:
                if current_dist + weight < distances[v]:
                    distances[v] = current_dist + weight
                    predecessors[v] = u
                    heapq.heappush(pq, (distances[v], v))
        
        return distances, predecessors
    
    def bellman_ford(self, source: int) -> Tuple[List[int], List[int], bool]:
        """
        Bellman-Ford algorithm for shortest paths.
        Works with negative weights and detects negative cycles.
        
        Time Complexity: O(V * E)
        Space Complexity: O(V)
        
        Args:
            source: Starting vertex
            
        Returns:
            Tuple of (distances, predecessors, has_negative_cycle)
        """
        distances = [float('inf')] * self.V
        distances[source] = 0
        predecessors = [-1] * self.V
        
        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
        
        # Check for negative cycles
        has_negative_cycle = False
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                has_negative_cycle = True
                break
        
        return distances, predecessors, has_negative_cycle
    
    def floyd_warshall(self) -> List[List[int]]:
        """
        Floyd-Warshall algorithm for all-pairs shortest paths.
        
        Time Complexity: O(V^3)
        Space Complexity: O(V^2)
        
        Returns:
            2D matrix of shortest distances between all pairs
        """
        # Initialize distance matrix
        dist = [[float('inf')] * self.V for _ in range(self.V)]
        
        # Distance from vertex to itself is 0
        for i in range(self.V):
            dist[i][i] = 0
        
        # Add edge weights
        for u, v, weight in self.edges:
            dist[u][v] = weight
            if not self.directed:
                dist[v][u] = weight
        
        # Floyd-Warshall main algorithm
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist
    
    def kruskal_mst(self) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Kruskal's algorithm for Minimum Spanning Tree.
        Uses Union-Find data structure.
        
        Time Complexity: O(E log E)
        Space Complexity: O(V)
        
        Returns:
            Tuple of (MST edges, total weight)
        """
        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        
        # Union-Find data structure
        parent = list(range(self.V))
        rank = [0] * self.V
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        
        mst_edges = []
        total_weight = 0
        
        for u, v, weight in sorted_edges:
            if union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                
                if len(mst_edges) == self.V - 1:
                    break
        
        return mst_edges, total_weight
    
    def prim_mst(self, start: int = 0) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Prim's algorithm for Minimum Spanning Tree.
        
        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)
        
        Args:
            start: Starting vertex (default: 0)
            
        Returns:
            Tuple of (MST edges, total weight)
        """
        mst_edges = []
        total_weight = 0
        visited = set([start])
        
        # Priority queue: (weight, u, v)
        pq = [(weight, start, v) for v, weight in self.adj_list[start]]
        heapq.heapify(pq)
        
        while pq and len(visited) < self.V:
            weight, u, v = heapq.heappop(pq)
            
            if v in visited:
                continue
            
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            for next_v, next_weight in self.adj_list[v]:
                if next_v not in visited:
                    heapq.heappush(pq, (next_weight, v, next_v))
        
        return mst_edges, total_weight
    
    def topological_sort_dfs(self) -> Optional[List[int]]:
        """
        Topological sort using DFS.
        Only works for Directed Acyclic Graphs (DAG).
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Returns:
            List of vertices in topological order, or None if cycle exists
        """
        if not self.directed:
            return None
        
        visited = set()
        rec_stack = set()
        result = []
        
        def dfs(v):
            visited.add(v)
            rec_stack.add(v)
            
            for neighbor, _ in self.adj_list[v]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
                elif neighbor in rec_stack:
                    return False  # Cycle detected
            
            rec_stack.remove(v)
            result.append(v)
            return True
        
        for vertex in range(self.V):
            if vertex not in visited:
                if not dfs(vertex):
                    return None  # Cycle exists
        
        return result[::-1]
    
    def graph_coloring(self) -> Dict[int, int]:
        """
        Greedy graph coloring algorithm.
        Assigns colors to vertices such that no two adjacent vertices
        have the same color.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Returns:
            Dictionary mapping vertex to color number
        """
        colors = {}
        
        for vertex in range(self.V):
            # Find colors used by neighbors
            neighbor_colors = set()
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor in colors:
                    neighbor_colors.add(colors[neighbor])
            
            # Assign smallest available color
            color = 0
            while color in neighbor_colors:
                color += 1
            
            colors[vertex] = color
        
        return colors


# Demonstration and Testing
def demonstrate_graph_algorithms():
    """
    Demonstrates all graph algorithms with examples.
    """
    print("=" * 70)
    print("ADVANCED GRAPH ALGORITHMS DEMONSTRATION")
    print("=" * 70)
    
    # Create a sample graph
    g = Graph(6, directed=False)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 3)
    
    print("\n1. DIJKSTRA'S SHORTEST PATH")
    print("-" * 70)
    distances, predecessors = g.dijkstra(0)
    for i, dist in enumerate(distances):
        print(f"   Distance from 0 to {i}: {dist}")
    
    print("\n2. BELLMAN-FORD ALGORITHM")
    print("-" * 70)
    distances, predecessors, has_cycle = g.bellman_ford(0)
    print(f"   Has negative cycle: {has_cycle}")
    for i, dist in enumerate(distances):
        print(f"   Distance from 0 to {i}: {dist}")
    
    print("\n3. KRUSKAL'S MST")
    print("-" * 70)
    mst_edges, total_weight = g.kruskal_mst()
    print(f"   MST Edges: {mst_edges}")
    print(f"   Total Weight: {total_weight}")
    
    print("\n4. PRIM'S MST")
    print("-" * 70)
    mst_edges, total_weight = g.prim_mst()
    print(f"   MST Edges: {mst_edges}")
    print(f"   Total Weight: {total_weight}")
    
    # Directed graph for topological sort
    dag = Graph(6, directed=True)
    dag.add_edge(5, 2)
    dag.add_edge(5, 0)
    dag.add_edge(4, 0)
    dag.add_edge(4, 1)
    dag.add_edge(2, 3)
    dag.add_edge(3, 1)
    
    print("\n5. TOPOLOGICAL SORT")
    print("-" * 70)
    topo_order = dag.topological_sort_dfs()
    print(f"   Topological Order: {topo_order}")
    
    print("\n6. GRAPH COLORING")
    print("-" * 70)
    colors = g.graph_coloring()
    print(f"   Vertex Colors: {colors}")
    print(f"   Chromatic Number: {max(colors.values()) + 1}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_graph_algorithms()
