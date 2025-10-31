# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform In-Order Traversal to get a sorted list of values
        nums = []
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            nums.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)

        # Step 2: Build a Balanced BST from the sorted list
        # 
        def build_balanced_bst(l, r):
            # Base Case: If the left index exceeds the right index, the subarray is empty.
            if l > r:
                return None
            
            # Find the middle element to use as the root
            mid = (l + r) // 2
            
            # Create the root node
            root_node = TreeNode(nums[mid])
            
            # Recursively build the left subtree from the left half of the array
            root_node.left = build_balanced_bst(l, mid - 1)
            
            # Recursively build the right subtree from the right half of the array
            root_node.right = build_balanced_bst(mid + 1, r)
            
            return root_node

        # Start building the balanced BST using the entire sorted list
        return build_balanced_bst(0, len(nums) - 1)

# Example Usage (optional):
# unbalanced_root = TreeNode(1)
# unbalanced_root.right = TreeNode(2)
# unbalanced_root.right.right = TreeNode(3)
# unbalanced_root.right.right.right = TreeNode(4)
# 
# balanced_root = Solution().balanceBST(unbalanced_root)
# # The balanced_root structure will be:
# #       3
# #      / \
# #     2   4
# #    /
# #   1
# time complexity: O(n)
# space complexity: O(n)


