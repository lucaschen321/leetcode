/*
 * Solution to LeetCode Problem 31
 * Source: https://leetcode.com/problems/next-permutation/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Implementnext permutation, which rearranges numbers into the lexicographically
 * next greater permutation of numbers.If such arrangement is not possible, it must
 * rearrange it as the lowest possible order (ie, sorted in ascending order).The
 * replacement must bein-placeand use only constant extra memory.Here are some
 * examples. Inputs are in the left-hand column and its corresponding outputs are
 * in the right-hand column.1,2,3→1,3,23,2,1→1,2,31,1,5→1,5,1
 */

#include "leetcode.h"

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() <= 1) {
            return;
        }

        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                // swap nums[i] with min to the right of nums[i] that's greater
                // than nums[i] and in the rightmost position
                for (int j = nums.size() - 1; j >= i; j--){
                    if (nums[i] < nums[j]) {
                        swap (nums[i], nums[j]);
                        reverse(nums.begin() + i + 1, nums.end());
                        return;
                    }
                }
            }
        }
        reverse(nums.begin(), nums.end());
    }
};

int main() {
    Solution s;
    vector<int> n{4,1,3,2,2,1,0,0};
    s.nextPermutation(n);
    for (auto const& value : n) {
        std::cout << value << std::endl;
    }
}
