from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        dq = deque()
        serialization = ""

        if root:
            dq.append(root)
            serialization += str(root.val) + ","

        while dq:
            node = dq.popleft()

            if node.left:
                dq.append(node.left)
                serialization += str(node.left.val) + ","
            else:
                serialization += ","
            if node.right:
                dq.append(node.right)
                serialization += str(node.right.val) + ","
            else:
                serialization += ","

        serialization = serialization[:-1]  # OR serialization.strip(",")
        return serialization

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        dq = deque()
        dq.append(root)

        i = 1
        while i < len(data):
            node = dq.popleft()
            left, right = data[i], data[i + 1] if i + 1 < len(data) else ''  # Bounds check if stripping trailing ','

            if left:  # Not the empty string
                node.left = TreeNode(int(left))
                dq.append(node.left)

            if right:
                node.right = TreeNode(int(right))
                dq.append(node.right)

            i += 2

        return root
