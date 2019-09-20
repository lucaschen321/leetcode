from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            # Array in ascending order
            if nums[left] < nums[right]:
                return nums[left]

            middle = left + (right - left) // 2
            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                left += 1

        return nums[left]
