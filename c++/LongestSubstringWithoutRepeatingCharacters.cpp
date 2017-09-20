#include "leetcode.h"

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map <char, int> map;
        int max_length = 0, i = 0;
        // Strings at positions [i,j] never contain duplicates
        for (int j = 0; j < s.length(); j++) {
            // Move [i] as far right as possible
            if (map.find(s[j]) != map.end())
                i = max(map[s[j]] + 1, i);
            map[s[j]] = j;
            max_length = max(j - i + 1, max_length);
        }
        return max_length;
    }
};
