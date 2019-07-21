from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []

        if not nums:
            return [-1, -1]

        # Find first
        while (left != right):
            middle = left + (right - left) // 2  # Bias middle towards the left
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] >= target:
                right = middle

        ans.append(left if nums[left] == target else -1)

        left, right = 0, len(nums) - 1

        # Find last
        while (left != right):
            middle = left + (right - left + 1) // 2  # Bias middle towards the right
            if nums[middle] <= target:
                left = middle
            elif nums[middle] > target:
                right = middle - 1

        ans.append(right if nums[right] == target else - 1)

        return ans
