from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Use 2 stacks to keep track of current and next level. Using 2 stacks
        traverses the current level in the correct order, but need to keep track
        of level number to insert children in left-right or right-left order.
        """
        levels = []
        curr_level, next_level, num_level = [root] if root else [], [], 0

        # Traverse while there are still levels
        while curr_level:
            levels.append([node.val for node in curr_level])
            # Pop each element from the current level stack. Add children to
            # next level stack.
            while curr_level:
                node = curr_level.pop()
                if num_level % 2 == 0:  # next level is backwards
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
                else:  # next level is forwards
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            curr_level, next_level = next_level, []
            num_level += 1

        return levels
