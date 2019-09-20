from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Array in ascending order
        if nums[left] < nums[right]:
            return nums[left]

        # Array is pivoted
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] <= nums[right]:
                right = middle
            else:
                left = middle + 1

        return nums[left]
