from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Walk over top-left quadrant and rotate each element with the three
        corresponding elements in the three other quadrants. When n (side
        length) is odd, include one of the quadrant boundaries, but not the
        other, or else the quadrant boundary will be rotated twice.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]
        return matrix
