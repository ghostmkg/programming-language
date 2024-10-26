// burning tree

import java.util.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solution
{
    public static int minTime(Node root, int target) 
    {
        Map<Node, Node> parentMap = new HashMap<>();
        Node targetNode = mapParents(root, parentMap, target);
        return bfsToBurnTree(targetNode, parentMap);
    }
    
    private static Node mapParents(Node root, Map<Node, Node> parentMap, int target) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        Node targetNode = null;
        
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            
            if (current.data == target) {
                targetNode = current;
            }
            
            if (current.left != null) {
                parentMap.put(current.left, current);
                queue.add(current.left);
            }
            
            if (current.right != null) {
                parentMap.put(current.right, current);
                queue.add(current.right);
            }
        }
        
        return targetNode;
    }
    
    private static int bfsToBurnTree(Node targetNode, Map<Node, Node> parentMap) {
        Queue<Node> queue = new LinkedList<>();
        Set<Node> visited = new HashSet<>();
        
        queue.add(targetNode);
        visited.add(targetNode);
        
        int time = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean burned = false;
            
            for (int i = 0; i < size; i++) {
                Node current = queue.poll();
                
                if (current.left != null && !visited.contains(current.left)) {
                    queue.add(current.left);
                    visited.add(current.left);
                    burned = true;
                }
                
                if (current.right != null && !visited.contains(current.right)) {
                    queue.add(current.right);
                    visited.add(current.right);
                    burned = true;
                }
                
                Node parent = parentMap.get(current);
                if (parent != null && !visited.contains(parent)) {
                    queue.add(parent);
                    visited.add(parent);
                    burned = true;
                }
            }
            
            if (burned) {
                time++;
            }
        }
        
        return time;
    }
}

class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}
