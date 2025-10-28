# Definition for a binary tree node (LeetCode).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CodecDFS:
    SEP = ','      # separator between tokens
    NULL = '#'     # null marker

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string using preorder DFS."""
        parts = []
        def dfs(node):
            if node is None:
                parts.append(self.NULL)
                return
            parts.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.SEP.join(parts)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes the string back to the original tree."""
        if not data:
            return None
        tokens = data.split(self.SEP)
        self.i = 0
        def build():
            if self.i >= len(tokens):
                return None
            tok = tokens[self.i]
            self.i += 1
            if tok == self.NULL:
                return None
            node = TreeNode(int(tok))
            node.left = build()
            node.right = build()
            return node
        return build()
