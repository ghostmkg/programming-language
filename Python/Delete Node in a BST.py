'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
def successer(root):
    if root.left is None:
        return root
    return successer(root.left)

def deleteNode(root, key):
    if root is None:
        return root
    if root.val > key:
        root.left = deleteNode(root.left,key)
        return root
    elif root.val < key:
        root.right = deleteNode(root.right,key)
        return root
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            suc = successer(root.right)
            root.val = suc.val
            root.right = deleteNode(root.right, suc.val)
            return root