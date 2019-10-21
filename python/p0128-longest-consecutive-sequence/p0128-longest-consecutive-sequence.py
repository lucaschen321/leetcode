from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_sequence = 1
                current = num + 1
                while current in nums_set:
                    current += 1
                    current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
