from typing import List


# Solution 1: Keep track of running sum, resetting if it gets less than 0.
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = -1 * float("inf"), 0
        for n in nums:
            current_sum += n
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum


# Solution 2: Kadane's algorithm. Modifies [nums] to contain the maximum
# subarray ending at i: it's max(nums[i], nums[i] + nums[i - 1]) - either the
# maximum subarray sum ending at position i+1 includes the maximum subarray sum
# ending at position i as a prefix, or it doesn't .
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
