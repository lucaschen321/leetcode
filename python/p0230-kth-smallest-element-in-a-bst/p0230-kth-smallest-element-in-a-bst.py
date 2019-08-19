# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Recursive inorder traversal.
class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count, ans = 1, 0

        def traverse(node):
            nonlocal count
            nonlocal ans
            if node.left:
                traverse(node.left)
            if count == k:
                ans = node.val
            count = count + 1
            if node.right:
                traverse(node.right)
            return

        traverse(root)
        return ans


# Solution 2: Iterative inorder traversal using a stack with early stopping.
class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        current, stack, count = root, [], 1

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if count == k:
                    return current.val
                count += 1
                current = current.right
        return count
