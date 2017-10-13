/*
 * Solution to LeetCode Problem 22
 * Source: https://leetcode.com/problems/generate-parentheses/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given n pairs of parentheses, write a function to generate all combinations of
 * well-formed parentheses.
 *
 *
 * For example, given n = 3, a solution set is:
 *
 * [
 *   "((()))",
 *   "(()())",
 *   "(())()",
 *   "()(())",
 *   "()()()"
 * ]
 */

import java.util.*;

public class GenerateParentheses {

    // Doesn't work because of order in which list is generated doesn't match
    // LeetCode's solution. It is otherwise, correct
    /* public static List<String> generateParenthesis(int n) {
    /     List<String> ans = new ArrayList<>();
    /     ans.add("()");
    /     String degenerate = "()";
    /     for (int i = 1; i < n; i++) {
    /         // For each iteration, store the answer for (n == i)
    /         List<String> iParen = new ArrayList<>();
    /         for (int j = 0; j < ans.size(); j++) {
    /             if (degenerate.equals(ans.get(j))) {
    /                 iParen.add("(" + degenerate + ")");
    /                 iParen.add(degenerate + "()");
    /             }
    /             else {
    /                 iParen.add("(" + ans.get(j) + ")");
    /                 iParen.add(ans.get(j) + "()");
    /                 iParen.add("()" + ans.get(j));
    /             }
    /         }
    /         degenerate += "()";
    /         ans = iParen;
    /     }
    /     return ans;
    /
    / }
    */
    public static List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<String>();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    public static void backtrack(List<String> ans, String s, int open, int close, int n){
        if (s.length() == n * 2) {
            ans.add(s);
            return;
        }

        if (open < n) {
            backtrack(ans, s + "(", open + 1, close, n);
        }

        if (close < open) {
            backtrack(ans, s + ")", open, close + 1, n);
        }

    }

    public static void main(String[] args) {
        List<String> ans = generateParenthesis(3);
        for (String s : ans) {
            System.out.println(s);
        }
    }

}
