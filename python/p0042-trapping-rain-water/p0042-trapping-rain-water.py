from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_on_left, max_on_right, trapped_water = 0, 0, 0
        left, right = 0, len(height) - 1

        while left <= right:
            if height[left] < height[right]:
                max_on_left = max(height[left], max_on_left)
                trapped_water += max_on_left - height[left]
                left += 1
            else:
                max_on_right = max(height[right], max_on_right)
                trapped_water += max_on_right - height[right]
                right -= 1

        return trapped_water
