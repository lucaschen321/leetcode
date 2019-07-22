# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # BST is valid if inorder traversal is in order from smallest to largest
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
