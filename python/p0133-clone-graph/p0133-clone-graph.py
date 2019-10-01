from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dq = deque([node])
        root = Node(node.val, [])
        original_to_copy = {node: root}

        while dq:
            curr_node = dq.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in original_to_copy:  # not yet visited or not in queue
                    dq.append(neighbor)

                copy_node = Node(neighbor.val, []) if neighbor not in original_to_copy else original_to_copy[neighbor]
                original_to_copy[neighbor] = copy_node
                original_to_copy[curr_node].neighbors.append(copy_node)

        return root
