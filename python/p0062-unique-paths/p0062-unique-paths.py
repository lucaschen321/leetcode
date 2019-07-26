import math


# Solution 1: Maintain DP array of number unique paths to (m,n).
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths_array = [[1] * m] * n
        for i in range(1, len(unique_paths_array)):
            for j in range(1, len(unique_paths_array[0])):
                unique_paths_array[i][j] = unique_paths_array[i - 1][j] + unique_paths_array[i][j - 1]

        return unique_paths_array[n - 1][m - 1]


# Solution 2: Each path from (0, 0) to (n - 1, m - 1) is a sequence of m - 1 horizontal steps and n - l vertical steps. There are C(n + m - 2, n - 1) steps.
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use integer division to avoid imprecision
        return int(math.factorial(m + n - 2) // math.factorial(n - 1) // math.factorial(m - 1))
