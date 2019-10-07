from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        level_size = 1  # keep track of the number of nodes in previous level
        dq = deque()

        if root:
            dq.append(root)
            levels.append([root.val])

        while dq:
            node = dq.popleft()
            level_size -= 1

            if node.left:
                dq.append(node.left)

            if node.right:
                dq.append(node.right)

            if level_size == 0 and dq:  # all nodes in previous level popped - add list(dq) to [levels]
                level_size = len(dq)
                levels.append([node.val for node in list(dq)])

        return levels
