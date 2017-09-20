#include "leetcode.h"

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int l, r, magnitude = 1;
        while ( x / magnitude >= 10) {
            magnitude *= 10;
        }

        while (x > 0) {
            l = x / magnitude;
            r = x % 10;
            if (r != l)
                return false;
            x = (x % magnitude) / 10;
            magnitude /= 100;
        }
        return true;
    }
};
