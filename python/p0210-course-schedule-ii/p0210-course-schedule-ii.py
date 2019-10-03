from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            nonlocal cycle_found
            if cycle_found:  # Don't recurse further if we found a cycle already
                return

            visited.add(node)
            # Traverse on neighboring vertices
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in visited and neighbor not in ordering:
                    # Edge to a neighbor in visited and not in ordering is a cycle
                    cycle_found = True

            # Recursion ends, so add to ordering
            ordering.append(node)

        # Convert edges to graph
        graph = defaultdict(list)
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        visited = set()
        ordering = []
        cycle_found = False

        for node in range(numCourses):
            # If node isn't visited (including isolated nodes), call dfs on it
            if node not in visited:
                dfs(node)
        ordering.reverse()

        return [] if cycle_found else ordering
