from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        candidates = [A[0], B[0]]
        for i in range(len(A)):
            candidates = [c for c in candidates if c in (A[i], B[i])]

        if not candidates:
            return -1

        return len(A) - max(A.count(candidates[0]), B.count(candidates[0]))
