from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Find min index where len(citations) - i <= citations[i].
        left, right = 0, len(citations) - 1

        # left < right instead of left != right for case where citations is []
        while left < right:
            middle = left + (right - left) // 2
            if len(citations) - middle <= citations[middle]:
                right = middle
            else:
                left = middle + 1

        # min(len(citations) - left, citations[left]) = len(citations) - left
        return len(citations) - left if citations else 0
