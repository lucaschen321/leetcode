#include "leetcode.h"
using namespace std;


class Solution {
public:
    int reverse(int x) {
        string s = to_string(abs(x));
        bool nonnegative = x >= 0;
        std::reverse(s.begin(), s.end());
        long result = stol(s);
        if (!nonnegative)
            result *= -1;
        if (result < -2147483648 || result > 2147483647)
            return 0;
        return (int) result;
    }
};
