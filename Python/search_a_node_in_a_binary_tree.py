'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def search(root, key):
    if root is None:
        return 0
    elif root.val == key:
        return 1
    elif search(root.left , key) == 1:
        return 1
    elif search(root.right,key) == 1:
        return 1
    return 0

