from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # DFS from (i,j), marking visited cells in [flow_matrix]
        def dfs(i, j, flow_matrix):
            if flow_matrix[i][j]:
                return
            else:
                flow_matrix[i][j] = True

                # Left
                if i - 1 >= 0 and not flow_matrix[i - 1][j] and matrix[i][j] <= matrix[i - 1][j]:
                    dfs(i - 1, j, flow_matrix)
                # Up
                if j - 1 >= 0 and not flow_matrix[i][j - 1] and matrix[i][j] <= matrix[i][j - 1]:
                    dfs(i, j - 1, flow_matrix)
                # Right
                if i + 1 < len(matrix) and not flow_matrix[i + 1][j] and matrix[i][j] <= matrix[i + 1][j]:
                    dfs(i + 1, j, flow_matrix)
                # Down
                if j + 1 < len(matrix[0]) and not flow_matrix[i][j + 1] and matrix[i][j] <= matrix[i][j + 1]:
                    dfs(i, j + 1, flow_matrix)

        pacific_flow = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        atlantic_flow = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        can_flow_to_both = []

        if not matrix:
            return can_flow_to_both

        # DFS from all cells on the perimeter
        for i in range(len(matrix)):
            dfs(i, 0, pacific_flow)
            dfs(i, len(matrix[0]) - 1, atlantic_flow)
        for j in range(len(matrix[0])):
            dfs(0, j, pacific_flow)
            dfs(len(matrix) - 1, j, atlantic_flow)

        # Add cell if it can flow to both pacific and atlantic
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific_flow[i][j] and atlantic_flow[i][j]:
                    can_flow_to_both.append([i, j])

        return can_flow_to_both
