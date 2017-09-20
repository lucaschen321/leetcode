#include "leetcode.h"
using namespace std;

// 0       2n - 2
// .      .
// .     .
// .    n
// n - 1

class Solution {
public:
    string convert(string s, int numRows) {
        string ans = "";
        int row_complement, row_temp, column;
        int modulus = numRows == 1 ? 1 : 2 * numRows - 2;
        for (int row = 0; row < numRows; row++) {
            row_complement = modulus - row;
            row_temp = row;
            column = row_temp;
            while (column < s.size()) {
                ans += s.at(column);
                if (column == row_temp) {
                    row_temp += modulus;
                }
                if (column == row_complement){
                    row_complement += modulus;
                }
                column = min(row_temp, row_complement);
            }
        }
        return ans;

    }
};
