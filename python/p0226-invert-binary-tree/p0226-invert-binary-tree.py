from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Recursive solution.
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right) if root.right else None,
                self.invertTree(root.left) if root.left else None,
            )
        return root


# Solution 2: Iterative solution a queue to traverse, swapping children for each node.
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        q.append(root)
        while q and root:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
