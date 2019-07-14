from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        print(nums)
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        write_ptr = 0
        for i in range(len(nums)):
            if not nums[write_ptr] == nums[i]:
                write_ptr = write_ptr + 1
                nums[write_ptr] = nums[i]
        nums[:] = nums[:write_ptr + 1]
        return len(nums)
