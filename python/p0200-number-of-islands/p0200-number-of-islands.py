from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, row, col):
            # BFS, marking visited cells with -1
            queue = [(row, col)]
            while queue:
                # Technically not BFS, since we pop and append to back of queue.
                row, col = queue.pop()
                if 0 < row and grid[row - 1][col] == "1":
                    grid[row - 1][col] = "-1"
                    queue.append((row - 1, col))
                if 0 < col and grid[row][col - 1] == "1":
                    grid[row][col - 1] = "-1"
                    queue.append((row, col - 1))
                if row + 1 < len(grid) and grid[row + 1][col] == "1":
                    grid[row + 1][col] = "-1"
                    queue.append((row + 1, col))
                if col + 1 < len(grid[0]) and grid[row][col + 1] == "1":
                    grid[row][col + 1] = "-1"
                    queue.append((row, col + 1))
                grid[row][col] = "-1"

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            grid[row][col] = "-1"
            dfs(grid, row - 1, col)
            dfs(grid, row, col - 1)
            dfs(grid, row + 1, col)
            dfs(grid, row, col + 1)

        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(grid, row, col)
                    num_islands += 1

        return num_islands
