/*
 * Solution to LeetCode Problem 72
 * Source: https://leetcode.com/problems/edit-distance/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given two wordsword1andword2, find the minimum number of operations required to
 * convertword1toword2.You have the following 3 operations permitted on a
 * word:Insert a characterDelete a characterReplace a characterExample
 * 1:Input:word1 = "horse", word2 = "ros"Output:3Explanation:horse -> rorse
 * (replace 'h' with 'r')
 * rorse -> rose (remove 'r')
 * rose -> ros (remove 'e')Example 2:Input:word1 = "intention", word2 =
 * "execution"Output:5Explanation:intention -> inention (remove 't')
 * inention -> enention (replace 'i' with 'e')
 * enention -> exention (replace 'n' with 'x')
 * exention -> exection (replace 'n' with 'c')
 * exection -> execution (insert 'u')
 */

#include "leetcode.h"

class Solution {
public:
    int minDistance(string word1, string word2) {
        // DP array storing edit distance between first i characters of [word1]
        // and first j characters of [word2]
        vector<vector<int>> editDistance(word1.length() + 1, vector<int>(word2.length() + 1, 0));
        for (int i = 0; i < word1.length() + 1; i++) {
            for (int j = 0; j < word2.length() + 1; j++) {
                // Initialization: For 0-indexed rows/columns, the value in the
                // cell is the index of the corresponding column/row
                if (i == 0 || j == 0) {
                    editDistance[i][j] = i + j;
                }
                // Fill in matrix: Updated distance is the min cost of
                // {deletion, insertion, subsitution}
                else {
                    int different_char = 0;
                    if (word1[i-1] != word2[j-1]) {
                        different_char = 1;
                    }
                    editDistance[i][j] = min({
                                        editDistance[i-1][j] + 1,
                                        editDistance[i][j-1] + 1,
                                        editDistance[i-1][j-1] + different_char
                                });
                }

            }
        }

        return editDistance[word1.length()][word2.length()];
    }
};
