from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        write = 0

        for index, element in enumerate(intervals[1:], 1):
            if intervals[write][1] >= element[0]:
                intervals[write][1] = max(intervals[write][1], element[1])
            else:
                write += 1
                intervals[write] = element

        return intervals[:write + 1]
