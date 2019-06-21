/*
 * Solution to LeetCode Problem 56
 * Source: https://leetcode.com/problems/merge-intervals/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a collection of intervals, merge all overlapping intervals.
 * Example 1:
 * Input: [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
 *
 * Example 2:
 * Input: [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
 */

#include "leetcode.h"

// Definition for an interval.
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        // Sort based on start time
        sort(intervals.begin(), intervals.end(), [] (Interval i1, Interval i2){
                                                return i1.start < i2.start;});
        int current = 0;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[current].end >= intervals[i].start) {
                intervals[current].end = max(intervals[current].end, intervals[i].end);
            } else {
                current++;
                intervals[current] = intervals[i];
            }
        }

        intervals.erase(intervals.begin() + current + 1, intervals.end());

        return intervals;
    }
};

int main() {
    Solution s;
    vector<Interval> v {};
    s.merge(v);
}
