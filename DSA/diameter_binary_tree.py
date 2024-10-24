class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def diameter(self, root):
        
        self.diameter_length = 0
        self.calculate_height(root)
        return self.diameter_length

    def calculate_height(self, node):
        if not node:
            return 0

      
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)

        
        self.diameter_length = max(self.diameter_length, left_height + right_height)

        
        return max(left_height, right_height) + 1

    def insert(self, value):
        """Inserts a value into the binary tree (for simplicity, as a BST)."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)


if __name__ == "__main__":
    bt = BinaryTree()
    
    
    nodes = [1, 2, 3, 4, 5]
    bt.root = TreeNode(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)

    print("Diameter of the binary tree:", bt.diameter(bt.root))
