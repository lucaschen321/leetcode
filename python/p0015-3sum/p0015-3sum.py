from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:  # skip duplicate elements
                # i + 1, since we don't need to check prior elements (we've already checked those combinations)
                low, high = i + 1, len(nums) - 1
                while low < high:
                    moving_sum = nums[low] + nums[i] + nums[high]
                    if moving_sum < 0:
                        low += 1
                    elif moving_sum > 0:
                        high -= 1
                    else:
                        solution.append(sorted([nums[low], nums[i], nums[high]]))
                        low += 1
                        high -= 1
                        # Advance pointers while elements are the same previous elements.
                        while nums[low] == nums[low - 1] and low < high:
                            low += 1
                        while nums[high] == nums[high + 1] and low < high:
                            high -= 1
        return solution
