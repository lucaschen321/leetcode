from typing import List


# Dynamic Programming Solution
class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]  # side length of maximal square ending here (bottom right ending here)
        max_square = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    above = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    above_left = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = min(above, left, above_left) + 1

                max_square = max(max_square, dp[i][j])

        return max_square ** 2


# Optimized Dynamic Programming Solution
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0 for j in range(len(matrix[0]))] if matrix else []  # side length of maximal square ending here (bottom right ending here)
        max_square = 0

        for i in range(len(matrix)):
            above_left = 0
            for j in range(len(matrix[0])):
                above = dp[j]
                left = dp[j - 1] if j > 0 else 0
                dp[j] = min(above, left, above_left) + 1 if matrix[i][j] == "1" else 0  # When matrix[i][j], the value in the dp array must be assigned to 0 (may not have been 0 previously)
                above_left = above

                max_square = max(max_square, dp[j])

        return max_square ** 2
