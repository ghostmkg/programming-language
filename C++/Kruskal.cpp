#include <iostream>
#include <vector>
#include <list>
#include <climits>
#include <algorithm>
using namespace std;
class DisjointSet
{
public:
    vector<int> parent;
    DisjointSet(int n)
    {
        parent.resize(n + 1, -1); // n+1 because we are storing 1 in index 1 (Not zero based indexing but 1 based indexing)
    }
    int findParent(int a)
    {
        if (parent[a] < 0)
            return a;
        return parent[a] = findParent(parent[a]);
    }
    void Union(int a, int b)
    {
        int pU = findParent(a);
        int pV = findParent(b);
        if (pU == pV)
            return;
        if ((parent[pU]) < (parent[pV])) // we do this because we consider more negative one as parent (-5 < -2)
        {
            parent[pU] += parent[pV];
            parent[pV] = pU;
        }
        else
        {
            parent[pV] += parent[pU];
            parent[pU] = pV;
        }
        return;
    }
};
class node
{
public:
    int data;
    int weight;
    node(int data, int weight) : data(data), weight(weight)
    {
    }
};
class Graph
{
public:
    vector<list<node>> G;
    int n;
    Graph(int n) : n(n), G(n)
    {
    }
    int weight(int u, int v)
    {
        for (auto node : G[u])
        {
            if (node.data == v)
                return node.weight; // If there exists edge between two vertices we return the weight of edge
        }
        return INT_MAX; // If there is no edge between two vertices we return INT_MAX
    }
    void addEdge(int u, int v, int w, bool undirected = true)
    {
        if (weight(u, v) != INT_MAX)
            return; // Before adding a edge to a vertex we check if there already exists that edge
        G[u].push_back(node(v, w));
        if (undirected) // When graph is undirected
            G[v].push_back(node(u, w));
    }
    void print()
    {

        for (int i = 0; i < n; i++)
        {
            cout << "Node " << i << " -> ";
            for (auto &node : G[i])
            {
                cout << "(" << node.data << ", w=" << node.weight << ") ";
            }
            cout << "\n";
        }
    }
};
class Edge
{
    public:
    int u,v,w;
    Edge(int u,int v,int w):u(u),v(v),w(w)
    {}
};
Graph Kruskal(Graph G)
{
    vector<Edge> edges;
    for (int i = 0; i < G.G.size(); i++)
    {
        list<node> l = G.G[i];
        for (node n : l)
            if (i < n.data) // avoid duplicate edges
                edges.push_back(Edge(i,n.data,n.weight));
    }
    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b)
         { return a.w < b.w; });

    Graph MST(G.n);
    DisjointSet D(G.n);
    for (auto edge : edges)
    {
        int pU = D.findParent(edge.u);
        int pV = D.findParent(edge.v);
        if (pU != pV)
        {
            D.Union(edge.u,edge.v);
            MST.addEdge(edge.u, edge.v, edge.w);
        }
    }
    return MST;
}
int main()
{
    Graph G(5);
    G.addEdge(0, 1, 2);
    G.addEdge(0, 2, 1);
    G.addEdge(1, 2, 1);
    G.addEdge(1, 4, 2);
    G.addEdge (1, 3, 2);
    G.addEdge(3, 4, 1);
    Graph MST = Kruskal(G);
    MST.print();
    return 0;
}
                        
/*
Time complexity analysis

Here we manually made a list of edges from graph, but in usual implementation we pass list of edges
into function so we directly have list of edges. So we do not consider that time.

Lets say there are E edges
So to sort all edges it takes O(ElogE)
We traverse across all E edges =>O(E)
We check whether both vertices have same parent or not =>O(2*(4*alpha))
Union takes =>O(1)
Adding edge takes =>O(1)
So total time complexity => O(ElogE + E*(2*(4*alpha)+1+1)) ~ O(ElogE+constant*E) ~ O(ElogE)


Space Complexity analysis
O(n) //As generally we directly pass list of edges we are not considering that space here 
and we are not considering the space of MST which is result, the only extra space used is of DSU data structure which is O(n)

Output 
Node 0 -> (2, w=1) 
Node 1 -> (2, w=1) (4, w=2) 
Node 2 -> (0, w=1) (1, w=1) 
Node 3 -> (4, w=1) 
Node 4 -> (3, w=1) (1, w=2)
*/