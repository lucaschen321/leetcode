from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Solution 1: Naïve recursive solution.
class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        else:
            curr_node = TreeNode(preorder[0])
            inorder_root_index = inorder.index(curr_node.val)
            curr_node.left = self.buildTree(preorder[1:inorder_root_index + 1], inorder[0:inorder_root_index])
            curr_node.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])
            return curr_node


# Solution 2: Recursive solution using map to reduce lookup of inorder index.
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def construct_tree(pre_start, pre_end, in_start, in_end):
            if not preorder or pre_start == pre_end:
                return None
            else:
                curr_node = TreeNode(preorder[pre_start])
                inorder_root_index = inorder_mapping.get(curr_node.val) - in_start
                curr_node.left = construct_tree(pre_start + 1, pre_start + inorder_root_index + 1, in_start, in_start + inorder_root_index)
                curr_node.right = construct_tree(pre_start + inorder_root_index + 1, pre_end, in_start + inorder_root_index + 1, in_end)
                return curr_node

        inorder_mapping = {n: i for i, n in enumerate(inorder)}
        return construct_tree(0, len(preorder), 0, len(inorder))


# Solution 3: Iterative solution using a stack.
class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        preorder_ptr, inorder_ptr, stack = 1, 0, [root]

        while preorder_ptr < len(preorder):
            temp = None
            current = TreeNode(preorder[preorder_ptr])

            while stack and stack[-1].val == inorder[inorder_ptr]:
                temp = stack.pop()
                inorder_ptr += 1

            if temp:
                temp.right = current
            else:
                stack[-1].left = current
            stack.append(current)
            preorder_ptr += 1

        return root
