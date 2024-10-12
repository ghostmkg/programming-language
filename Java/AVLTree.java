package BinaryTrees;

public class AVL {
    int count = 5;
    public class Node{
        private int val;
        private int height;
        Node left;
        Node right;
        public Node(int val){
            this.val = val;
        }
        public int getVal(){
            return val;
        }
    }
    public Node root;
    public int height(Node node){
        if(node==null){
            return -1;
        }
        return node.height;
    }
    public boolean isEmpty(){
        return root==null;
    }
    public void insert(int val){
        root = insert(root,val);
    }
    public Node insert(Node node,int val){
        if(node==null){
            node = new Node(val);
            return node;
        }
        if(node.val>val){
            node.left = insert(node.left,val);
        }
        if(node.val<val) {
            node.right = insert(node.right, val);
        }
        node.height = Math.max(height(node.left),height(node.right))+1;
        return rotate(node);
    }
    private Node rotate(Node node){
        if(height(node.left)-height(node.right)>1){
            //left heavy
            if(height(node.left.left)-height(node.left.right)>0){
                return rightRotate(node);
            }
            if(height(node.left.left)-height(node.left.right)<0){
                node.left = leftRotate(node.left);
                return rightRotate(node);
            }
        }
        if((height(node.left) - height(node.right)) < -1){
            //right heavy
            if(height(node.right.left)-height(node.right.right)<0){
                return leftRotate(node);
            }
            if(height(node.right.left)-height(node.right.right)>0){
                node.right = rightRotate(node.right);
                return leftRotate(node);
            }
        }
        return node;
    }
    public Node rightRotate(Node p){
        Node c = p.left;
        Node t = c.right;
        c.right = p;
        p.left = t;

        p.height = Math.max(height(p.left),height(p.right))+1;
        c.height = Math.max(height(c.left),height(c.right))+1;

        return c;
    }
    public Node leftRotate(Node p){
        Node c = p.right;
        Node t = c.left;
        c.left = p;
        p.right = t;

        p.height = Math.max(height(p.left),height(p.right))+1;
        c.height = Math.max(height(c.left),height(c.right))+1;
        return c;
    }
    public void display(){
        display2D(root,0);
    }
    public void display2D(Node root, int space){
        if(root==null){
            return;
        }
        space+=count;
        display2D(root.right,space);
        System.out.println();
        for(int i=count;i<space;i++){
            System.out.print(" ");
        }
        System.out.println(root.val);
        display2D(root.left,space);
    }
    public void populateSorted(int[] nums){
        populateSorted(nums,0,nums.length);
    }
    public void populateSorted(int[] nums,int s,int e){
        if(s>=e){
            return ;
        }
        int mid = (s+e)/2;
        this.insert(nums[mid]);
        populateSorted(nums,s,mid);
        populateSorted(nums,mid+1,e);
    }
    public boolean isBalanced(Node node){
        if(node==null){
            return true;
        }
        return Math.abs(height(node.left)-height(node.right))<=1 && isBalanced(node.left) && isBalanced(node.right);
    }
}
