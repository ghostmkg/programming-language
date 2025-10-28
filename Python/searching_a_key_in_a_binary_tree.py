'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def search_in_bst(root, key):
    if root is None:
        return 0
    elif root.val == key:
        return 1
    elif search_in_bst(root.left,key) == 1:
        return 1
    elif search_in_bst(root.right,key) == 1:
        return 1
    return 0


