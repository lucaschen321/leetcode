from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array, product = [], 1

        # Forward pass
        for num in nums:
            product_array.append(product)
            product *= num

        # Backward pass
        product = 1
        for i in reversed(range(len(nums))):
            product_array[i] *= product
            product *= nums[i]

        return product_array
