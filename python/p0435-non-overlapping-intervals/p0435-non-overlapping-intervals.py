from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        previous_interval_end, max_non_overlapping = float("-inf"), 0
        for interval in intervals:
            if interval[0] >= previous_interval_end:
                previous_interval_end = interval[1]
                max_non_overlapping += 1

        return len(intervals) - max_non_overlapping
