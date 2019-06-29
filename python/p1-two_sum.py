#
# Solution to LeetCode Problem 1
# Source: https://leetcode.com/problems/two-sum/
# Author: Lucas Chen
#

"""
Description:
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

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
