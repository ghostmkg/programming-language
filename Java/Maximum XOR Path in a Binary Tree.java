import java.util.*;

class Node {
    int val;
    Node left, right;
    Node(int v) { val = v; }
}

public class MaxXORPath {
    static int maxXor = 0;
    static List<Integer> pathVals = new ArrayList<>();

    static void dfs(Node node, int currXor) {
        if (node == null) return;
        currXor ^= node.val;
        pathVals.add(currXor);
        maxXor = Math.max(maxXor, currXor);
        dfs(node.left, currXor);
        dfs(node.right, currXor);
    }

    public static void main(String[] args) {
        Node root = new Node(5);
        root.left = new Node(1);
        root.right = new Node(7);
        root.left.left = new Node(3);
        root.right.left = new Node(6);
        dfs(root, 0);
        for (int i : pathVals)
            for (int j : pathVals)
                maxXor = Math.max(maxXor, i ^ j);
        System.out.println("Max XOR Path Value: " + maxXor);
    }
}
