# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Comparison of Nodes: Check whether each node in s is the same tree as t.
class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same_tree(s, t):
            if not s and not t:
                return True
            elif s and t:
                return s.val == t.val and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

            return False

        if is_same_tree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) if s else False


# Solution2: Use Preorder Traversal
class Solution2:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def generate_preorder_string(root):
            s = ""
            if not root:
                s += ",null"
            else:
                s += "," + str(root.val)
                s += generate_preorder_string(root.left)
                s += generate_preorder_string(root.right)

            return s

        s_string = generate_preorder_string(s)
        t_string = generate_preorder_string(t)

        return t_string in s_string
