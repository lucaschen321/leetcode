from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive solution.
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Iterative solution using a stack.
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        current = root
        ordering = []

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                ordering.append(current.val)
                current = current.right

        return ordering
