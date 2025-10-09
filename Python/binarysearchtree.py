class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # Delete a key
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            min_node = self._minValueNode(root.right)
            root.key = min_node.key
            root.right = self._delete(root.right, min_node.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Inorder Traversal (sorted order)
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        return self._inorder(root.left) + [root.key] + self._inorder(root.right) if root else []


# Example usage
if __name__ == "__main__":
    bst = BST()
    elements = list(map(int, input("Enter numbers to insert (space-separated): ").split()))
    for el in elements:
        bst.insert(el)

    print("Inorder Traversal:", bst.inorder())

    key = int(input("Enter a value to search: "))
    print("Found!" if bst.search(key) else "Not found.")

    delete_key = int(input("Enter a value to delete: "))
    bst.delete(delete_key)
    print("Inorder Traversal after deletion:", bst.inorder())
