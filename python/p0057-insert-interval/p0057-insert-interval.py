from typing import List


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or intervals[-1][1] < newInterval[0]:  # Interval to be inserted at back
            intervals.append(newInterval)
        elif newInterval[1] < intervals[0][0]:  # Interval to be inserted at beginning
            intervals.insert(0, newInterval)
        else:  # Interval to be inserted in middle
            # Binary search for left/right intervals to be merged with newInterval
            left, right = 0, len(intervals) - 1
            while left != right:
                middle = left + (right - left) // 2
                if newInterval[0] > intervals[middle][1]:
                    left = middle + 1
                else:
                    right = middle

            left_interval = left
            left, right = 0, len(intervals) - 1

            while left != right:
                middle = left + (right - left + 1) // 2
                if intervals[middle][0] <= newInterval[1]:
                    left = middle
                else:
                    right = middle - 1
            right_interval = left

            intervals[left_interval:right_interval + 1] = [[min(newInterval[0], intervals[left_interval][0]), max(newInterval[1], intervals[right_interval][1])]]

        return intervals


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        merged_intervals = newInterval
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif newInterval[1] < interval[0]:
                right.append(interval)
            else:
                merged_intervals[0], merged_intervals[1] = min(merged_intervals[0], interval[0]), max(merged_intervals[1], interval[1])

        return left + [merged_intervals] + right
