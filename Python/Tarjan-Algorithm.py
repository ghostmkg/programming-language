from collections import defaultdict

class TarjanSCC:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Dictionary to store the graph
        self.V = vertices  # Number of vertices
        self.time = 0  # Global variable for time
        self.low = [-1] * vertices  # Low-link values
        self.disc = [-1] * vertices  # Discovery times
        self.stack_member = [False] * vertices  # Stack member boolean array
        self.stack = []  # Stack to store visited vertices

    def add_edge(self, u, v):
        """Add an edge from vertex u to vertex v"""
        self.graph[u].append(v)

    def tarjan_scc_util(self, u):
        """A recursive function to find SCCs using Tarjan's Algorithm"""
        self.disc[u] = self.low[u] = self.time
        self.time += 1
        self.stack.append(u)
        self.stack_member[u] = True

        # Go through all vertices adjacent to u
        for v in self.graph[u]:
            if self.disc[v] == -1:  # If v is not visited yet
                self.tarjan_scc_util(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.stack_member[v]:  # If v is in the stack, it is part of SCC
                self.low[u] = min(self.low[u], self.disc[v])

        # If u is the root of an SCC
        if self.low[u] == self.disc[u]:
            scc = []
            while True:
                v = self.stack.pop()
                self.stack_member[v] = False
                scc.append(v)
                if v == u:
                    break
            print("SCC:", scc)

    def tarjan_scc(self):
        """Function to find all SCCs in the graph"""
        for i in range(self.V):
            if self.disc[i] == -1:
                self.tarjan_scc_util(i)

# Example Usage
g = TarjanSCC(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
g.tarjan_scc()
