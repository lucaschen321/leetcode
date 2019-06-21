/*
 * Solution to LeetCode Problem 76
 * Source: https://leetcode.com/problems/minimum-window-substring/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a string S and a string T, find the minimum window in S which will contain
 * all the characters in T in complexity O(n).Example:Input: S= "ADOBECODEBANC",T=
 * "ABC"Output:"BANC"Note:If there is no such window in S that covers all
 * characters in T, return the empty string"".If there is such window, you are
 * guaranteed that there will always be only one unique minimum window in S.
 */

#include "leetcode.h"

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> t_char_frequency;
        unordered_map<char, int> window_char_frequency;
        string ans = s;

        if (s.length() == 0 || t.length() == 0) {
            return "";
        }

        // Create t_char_frequency mapping of substring t
        for (int i = 0; i < t.length(); i++) {
            t_char_frequency[t[i]]++;
        }

        int formed = 0;

        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            window_char_frequency[s[r]]++;

            if (t_char_frequency.find(s[r]) != t_char_frequency.end() && window_char_frequency[s[r]] == t_char_frequency[s[r]]) {
                    formed++;
            }

            if (formed == t_char_frequency.size()) {
                while(t_char_frequency.find(s[l]) == t_char_frequency.end() || window_char_frequency[s[l]] > t_char_frequency[s[l]]){
                    window_char_frequency[s[l]]--;
                    l++;
                }
                ans = ans.length() > r - l + 1 ? s.substr(l, r - l + 1) : ans;
            }
        }
        if (formed != t_char_frequency.size()) {
            return "";
        }
        return ans;
    }
};

int main() {
    Solution s;
    cout << s.minWindow("adobe", "x") << endl;
}
