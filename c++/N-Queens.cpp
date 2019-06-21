/*
 * Solution to LeetCode Problem 51
 * Source: https://leetcode.com/problems/n-queens/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Then-queens puzzle is the problem of placingnqueens on ann×nchessboard such that
 * no two queens attack each other.Given an integern, return all distinct solutions
 * to then-queens puzzle.Each solution contains a distinct board configuration of
 * then-queens' placement, where'Q'and'.'both indicate a queen and an empty space
 * respectively.Example:Input:4Output:[
 *  [".Q..",  // Solution 1
 *   "...Q",
 *   "Q...",
 *   "..Q."],
 *
 *  ["..Q.",  // Solution 2
 *   "Q...",
 *   "...Q",
 *   ".Q.."]
 * ]Explanation:There exist two distinct solutions to the 4-queens puzzle as shown
 * above.
 */

#include "leetcode.h"

class Solution {
public:
    bool solveNQueens(int n) {
        map<int, int> rows;
        map<int, int> cols;
        int num_solutions = 0;

        for (int i = 0; i < n; i++)  {
            backtrack(0, i, rows, cols, n, num_solutions);
            cout << endl;
        }

        cout << num_solutions << endl;
        return false;
    }

    void backtrack(int r, int c, map<int, int> rows, map<int, int> cols, int n, int &num_solutions) {
        cout << r << " "<< c << endl;

        if (c == n) {
            return; // no solution
        }

        if (cols.find(c) == cols.end()) {
            for (map<int, int>::iterator it = cols.begin(); it != cols.end(); it++) {
                int column = it->first;
                if (abs(c-column) == abs(r-cols[column])){
                    // not a solution for that row (diagonal)
                    return;
                }
            }
            if (r == n-1) {
                num_solutions++;
                cout << "Solution!" << endl;
                return;
            }
            // found a solution for that row
            rows[r] = c;
            cols[c] = r;
            for (int i = 0; i < n && r - 1 < n; i++) {
                backtrack(r + 1, i, rows, cols, n, num_solutions);
            }
            rows.erase(r);
            cols.erase(c);

        }
    }

};
