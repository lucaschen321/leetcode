from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_container = 0, len(height) - 1, 0

        while left < right:
            max_container = max(max_container, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_container
