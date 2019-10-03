from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_path_sum_helper(root: TreeNode) -> Tuple[int, int]:
            if not root:
                return float("-inf"), 0
            else:
                left, right = max_path_sum_helper(root.left), max_path_sum_helper(root.right)
                return max(
                    left[0], right[0],
                    root.val + max(0, left[1]) + max(0, right[1])
                ), root.val + max(0, left[1], right[1])

        return max_path_sum_helper(root)[0]
