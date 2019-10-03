from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dq = deque([node])
        original_to_copy = {node: Node(node.val, [])}  # Map from vertices to counterparts in clone

        while dq:
            curr_node = dq.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in original_to_copy:  # not yet visited or not in queue
                    dq.append(neighbor)
                    original_to_copy[neighbor] = Node(neighbor.val, [])

                original_to_copy[curr_node].neighbors.append(original_to_copy[neighbor])

        return original_to_copy[node]
