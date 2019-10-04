# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive solution
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Iterative solution
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        max_height, stack = 0, []
        if root:
            stack.append((root, 1))

        while stack:
            current, current_height = stack.pop()
            if current.left:
                stack.append((current.left, current_height + 1))
            if current.right:
                stack.append((current.right, current_height + 1))

            max_height = max(current_height, max_height)

        return max_height
