/*
 * Solution to LeetCode Problem 42
 * Source: https://leetcode.com/problems/trapping-rain-water/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Givennnon-negative integers representing an elevation map where the width of
 * each bar is 1, compute how much water it is able to trap after raining.The above
 * elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6
 * units of rain water (blue section) are being trapped.Thanks Marcosfor
 * contributing this image!Example:Input:[0,1,0,2,1,0,1,3,2,1,2,1]Output:6
 */

#include "leetcode.h"

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) {
            return 0;
        }

        int max_so_far = height[0], water_trapped = 0;
        vector<int> max_left(height.size()); // stores the value of max height to the left of index

        for (auto i = 0; i < height.size(); i++) {
            max_so_far = max(max_so_far, height[i]);
            max_left[i] = max_so_far;
        }

        max_so_far = height[height.size()-1];
        for (int i = height.size() - 1; i >= 0; i--) {
            // loop from right to left, while keeping track of max height to
            // the right of index [max_so_far]
            // Water trapped an index = max(0, min(max_left,max_right) - height at i)
            max_so_far = max(max_so_far, height[i]);
            water_trapped += max(0, min(max_left[i], max_so_far) - height[i]);
        }

        return water_trapped;
    }
};
