from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive Solution
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if bool(p) ^ bool(q):
            # One of p and q is None
            return False
        elif not p and not q:
            # If both are None
            return True
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Iterative Solution
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p_node, q_node):
            # If both are None
            if not p_node and not q_node:
                return True
            # One of p and q is None
            if not p_node or not q_node:
                return False
            return p_node.val == q_node.val

        dq = deque([(p, q)])
        while dq:
            p_node, q_node = dq.popleft()

            if not check(p_node, q_node):
                return False

            if p_node:
                dq.append((p_node.left, q_node.left))
                dq.append((p_node.right, q_node.right))

        return True
