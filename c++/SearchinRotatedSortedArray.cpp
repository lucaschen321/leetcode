/*
 * Solution to LeetCode Problem 33
 * Source: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Suppose an array sorted in ascending order is rotated at some pivot unknown to
 * you beforehand.(i.e.,[0,1,2,4,5,6,7]might become[4,5,6,7,0,1,2]).You are given a
 * target value to search. If found in the array return its index, otherwise
 * return-1.You may assume no duplicate exists in the array.Your algorithm's
 * runtime complexity must be in the order ofO(logn).Example 1:Input:nums =
 * [4,5,6,7,0,1,2], target = 0Output:4Example 2:Input:nums = [4,5,6,7,0,1,2],
 * target = 3Output:-1
 */

#include "leetcode.h"

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return -1;
        }
        // Find pivot
        vector<int>::iterator begin = nums.begin();
        vector<int>::iterator end = nums.end();
        if  (nums.front() > nums.back()) {
            int pivot = find_pivot(nums, 0, nums.size() - 1);
            if (nums.front() <= target) {
                end = nums.begin() + pivot;
            } else {
                begin = nums.begin() + pivot + 1;
            }
        }

        int search_index = lower_bound(begin, end, target) - nums.begin();
        return nums[search_index] == target ? search_index : -1;
    }

    int find_pivot(vector<int>& nums, int left, int right)  {
        if (right - left == 1) {
            return left;
        }

        int middle = (left + right) / 2;
        if (nums[middle] > nums[right]) {
            return find_pivot(nums, middle, right);
        } else {
            return find_pivot(nums, left, middle);
        }

    }
};
