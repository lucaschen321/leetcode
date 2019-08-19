from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, ans, combination, target, i):
            if target < 0:
                return
            elif target == 0:
                ans.append(combination)
            else:
                # Don't include numbers before i to avoid duplicate combinations (e.g. [2, 2, 3] and [2, 3, 2])
                for enum_i, num in enumerate(candidates[i:], i):
                    backtrack(
                        candidates,
                        ans,
                        combination + [num],
                        target - num,
                        enum_i,
                    )

        combination, ans = [], []
        backtrack(candidates, ans, combination, target, 0)

        return ans
