#include <iostream>
#include <vector>
#include <list>
#include <climits>
#include <algorithm>
#include <queue>
using namespace std;

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

struct cmp
{
    bool operator()(Edge a,Edge b)
    {
        return a.w>b.w;
    }
};


Graph Prims(Graph G)
{
    priority_queue <Edge,vector<Edge>,cmp> p;
    vector<Edge> edges;
    vector<bool> visited(G.n,false);
    Graph MST(G.n);
    for (int i = 0; i < G.G.size(); i++)
    {
        list<node> l = G.G[i];
        for (node n : l)
            if (i < n.data) // avoid duplicate edges
                edges.push_back(Edge(i,n.data,n.weight));
    }
    Edge E(0,0,-1); //Taking zero as source
    p.push(E);
    while(p.size()>0)
    {
        //u is source and v is destination or u is parent and v is node
        Edge e=p.top();
        p.pop();
        if(visited[e.v]) continue;
        if(e.w!=-1)MST.addEdge(e.u,e.v,e.w);
        visited[e.v]=true;
        list<node> l = G.G[e.v];
        for(node n:l)
        {
            if(!visited[n.data])
            {
                Edge E(e.v,n.data,n.weight);
                p.push(E);
            }
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
    G.addEdge(1, 3, 2);
    G.addEdge(3, 4, 1);
    Graph MST = Prims(G);
    MST.print();
    return 0;
}

/*
Time complexity analysis
Here we manually made a list of edges from graph, but in usual implementation we pass list of edges
into function so we directly have list of edges. So we do not consider that time.
Apart from that 
Pushing/poping operation takes O(logE) time
We push every edge and pop them
So total T.C=O(ElogE)

space complexity analysis
O(E+N)//O(E) for storing edges in priority queue [E is total number of edges, which we may add in worst case]
//O(N) for visited array

Output
Node 0 -> (2, w=1) 
Node 1 -> (2, w=1) (4, w=2) 
Node 2 -> (0, w=1) (1, w=1) 
Node 3 -> (4, w=1) 
Node 4 -> (1, w=2) (3, w=1)
*/