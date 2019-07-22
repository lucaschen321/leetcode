from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, ans, subset, i):
            if i == len(nums):  # End of nums has been reached
                ans.append(subset)
            else:
                backtrack(nums, ans, subset + [nums[i]], i + 1)  # All subsets that include nums[i]
                backtrack(nums, ans, subset, i + 1)  # All subsets that exclude nums[i]
            return

        ans, subset, i = [], [], 0
        backtrack(nums, ans, subset, i)

        return ans
