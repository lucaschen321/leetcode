/*
 * Solution to LeetCode Problem 139
 * Source: https://leetcode.com/problems/word-break/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a non-empty string s and a dictionary wordDict containing a list of non-
 * empty words, determine if s can be segmented into a space-separated sequence of
 * one or more dictionary words. You may assume the dictionary does not contain
 * duplicate words.
 *
 * For example, given
 * s = "leetcode",
 * dict = ["leet", "code"].
 *
 *
 * Return true because "leetcode" can be segmented as "leet code".
 *
 *
 * UPDATE (2017/1/4):
 * The wordDict parameter had been changed to a list of strings (instead of a set
 * of strings). Please reload the code definition to get the latest changes.
 */

import java.util.*;

public class WordBreak {
    public static boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dictionary = new HashSet<String>(wordDict);
        boolean[] canBreak = new boolean[s.length() + 1];

        for (int i = 1; i <= s.length(); i++) {
            if (canBreak[i] || dictionary.contains(s.substring(0, i))) {
                canBreak[i] = true;
                for (int j = i + 1; j <= s.length(); j++) {
                    if (dictionary.contains(s.substring(i, j))) {
                        canBreak[j] = true;
                    }
                }
            }
        }
        return canBreak[s.length()];
    }

    public static void main(String[] args) {
        String s = "twoone";
        List<String> wordDict = new ArrayList<String>(Arrays.asList("one", "two", " four"));
        System.out.println(wordBreak(s, wordDict));
    }

}
