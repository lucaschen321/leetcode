from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_encountered = {}  # map numbers to indices
        for i in range(len(nums)):
            if (target - nums[i] in nums_encountered):
                return [nums_encountered[target - nums[i]], i]
            else:
                nums_encountered[nums[i]] = i
        return []
