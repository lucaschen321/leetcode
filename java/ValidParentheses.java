/*
 * Solution to LeetCode Problem 20
 * Source: https://leetcode.com/problems/valid-parentheses/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid
 * but "(]" and "([)]" are not.
 */

import java.util.*;

public class ValidParentheses {

    public static boolean isValid(String s) {
        Map<String, String> parens = new HashMap<String, String>();
        parens.put("{", "}");
        parens.put("(", ")");
        parens.put("[", "]");
        Stack<String> stack = new Stack<String>();

        for (int i = 0; i < s.length(); i++) {
            if (parens.containsKey(s.substring(i, i + 1))) {
                stack.push(parens.get(s.substring(i, i + 1)));
            }
            else {
                if (stack.empty() || !stack.peek().equals(s.substring(i, i + 1))) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        return stack.empty();

    }

    // public static void main(String[] args) {
    //     String s = ")";
    //     System.out.println(isValid(s));
    // }

}
