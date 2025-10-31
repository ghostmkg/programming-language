import java.util.*;

class GraphNode {
    int val;
    Map<GraphNode, Integer> neighbors = new HashMap<>();
    GraphNode(int v) { val = v; }
}

public class CloneGraph {
    static GraphNode cloneGraph(GraphNode node, Map<GraphNode, GraphNode> map) {
        if (node == null) return null;
        if (map.containsKey(node)) return map.get(node);

        GraphNode clone = new GraphNode(node.val);
        map.put(node, clone);

        for (GraphNode neigh : node.neighbors.keySet())
            clone.neighbors.put(cloneGraph(neigh, map), node.neighbors.get(neigh));

        return clone;
    }

    public static void main(String[] args) {
        GraphNode a = new GraphNode(1);
        GraphNode b = new GraphNode(2);
        GraphNode c = new GraphNode(3);
        a.neighbors.put(b, 5);
        b.neighbors.put(c, 2);
        c.neighbors.put(a, 1);

        GraphNode clone = cloneGraph(a, new HashMap<>());
        System.out.println("Cloned node value: " + clone.val);
        System.out.println("Neighbor count: " + clone.neighbors.size());
    }
}
