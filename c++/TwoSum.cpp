#include "leetcode.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Key is the number and value is its index in the vector
        unordered_map <int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end()) {
                return {hash[complement], i};
            }
            else
                hash[nums[i]] = i;
        }
        return {0, 0};
    }
};
