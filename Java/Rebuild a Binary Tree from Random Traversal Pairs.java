import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class RebuildTree {
    static TreeNode buildTree(int[] preorder, int[] random) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < random.length; i++)
            map.put(random[i], i);
        return helper(preorder, 0, preorder.length - 1, random, 0, random.length - 1, map);
    }

    static TreeNode helper(int[] pre, int ps, int pe, int[] rand, int rs, int re, Map<Integer, Integer> map) {
        if (ps > pe || rs > re) return null;
        TreeNode root = new TreeNode(pre[ps]);
        int idx = map.get(pre[ps]);
        int leftSize = idx - rs;
        root.left = helper(pre, ps + 1, ps + leftSize, rand, rs, idx - 1, map);
        root.right = helper(pre, ps + leftSize + 1, pe, rand, idx + 1, re, map);
        return root;
    }

    public static void main(String[] args) {
        int[] preorder = {1,2,4,5,3,6,7};
        int[] random = {4,2,5,1,6,3,7};
        TreeNode root = buildTree(preorder, random);
        System.out.println("Root: " + root.val);
    }
}
