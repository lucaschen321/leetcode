from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = max_ending_here = min_ending_here = nums[0]
        for num in nums[1:]:
            max_ending_here, min_ending_here = (
                max(num, max_ending_here * num, min_ending_here * num),
                min(num, max_ending_here * num, min_ending_here * num),
            )
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
