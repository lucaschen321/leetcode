# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Recursive solution.
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = min(p.val, q.val), max(p.val, q.val)
        while not p_val <= root.val <= q_val:
            if root.val < p_val:
                root = root.right
            else:
                root = root.left

        return root


# Solution 2: Recursive solution.
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
