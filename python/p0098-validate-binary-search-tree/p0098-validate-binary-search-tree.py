# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: BST is valid if inorder traversal is in order from smallest to largest
class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        previous_node_val = float("-inf")

        def traverse(node):
            nonlocal previous_node_val
            valid_left = valid_node = valid_right = True
            if (node.left):
                valid_left = traverse(node.left)
            valid_node = previous_node_val < node.val
            previous_node_val = node.val
            if (node.right):
                valid_right = traverse(node.right)
            return valid_left and valid_node and valid_right

        return traverse(root) if root else True


# Solution 2: Check recursively that for each node, min_range < node.val < max_range
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        min_range, max_range = float("-inf"), float("inf")

        def traverse(node, min_range, max_range):
            if not node:
                return True
            elif not min_range < node.val < max_range:
                return False
            return traverse(node.left, min_range, node.val) and traverse(node.right, node.val, max_range)

        return traverse(root, min_range, max_range)
