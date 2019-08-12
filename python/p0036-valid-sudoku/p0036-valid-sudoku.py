from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRegion(region):
            """
            Helper function to check if flattened list has no duplicates, with
            all members between 1 and 9 (inclusive).
            """
            region = [n for n in region if n != "."]
            if len(region) != len(set(region)):
                return False
            return all(1 <= int(n) <= 9 for n in region)

        # Check that all rows are valid
        for row in board:
            if not isValidRegion(row):
                return False

        # Check that all columns are valid
        for i in range(9):
            if not isValidRegion([row[i] for row in board]):
                return False

        # Check that all regions/subgrids are valid
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                flattened_grid = [n for row in board[i:i + 3] for n in row[j:j + 3]]
                if not isValidRegion(flattened_grid):
                    return False

        return True
