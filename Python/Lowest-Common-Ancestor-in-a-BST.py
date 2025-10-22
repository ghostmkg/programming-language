class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA(root, n1, n2):
    def exists(node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        return exists(node.left, val) if val < node.val else exists(node.right, val)

    if not exists(root, n1) or not exists(root, n2):
        return Node(-1)

    current = root
    while current:
        if n1 < current.val and n2 < current.val:
            current = current.left
        elif n1 > current.val and n2 > current.val:
            current = current.right
        else:
            return current

