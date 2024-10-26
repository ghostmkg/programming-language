class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    # Insertion method
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # Search method
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # In-order Traversal (Sorted order)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    # Deletion method
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        # If key to be deleted is smaller than root's key, it lies in the left subtree
        if key < root.key:
            root.left = self._delete(root.left, key)
        # If key to be deleted is greater than root's key, it lies in the right subtree
        elif key > root.key:
            root.right = self._delete(root.right, key)
        # If key is the same as root's key, this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right).key
            # Delete the inorder successor
            root.right = self._delete(root.right, root.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example usage
if __name__ == "__main__":
    bst = BST()
    elements = [20, 10, 30, 5, 15, 25, 35]

    # Inserting elements
    for element in elements:
        bst.insert(element)

    print("In-order traversal after insertion:", bst.inorder())

    # Searching for an element
    key = 15
    result = bst.search(key)
    print(f"Element {key} found in BST?" , "Yes" if result else "No")

    # Deleting an element
    bst.delete(10)
    print("In-order traversal after deleting 10:", bst.inorder())
