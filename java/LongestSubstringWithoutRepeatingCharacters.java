/*
 * Solution to Leetcode Problem 3
 * Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Author: Lucas Chen
 */

/*
 * We can use a sliding window approach, where the characters in the substring
 * [i,j) are in the hashset. We increment j, adding each character to the
 * HashSet until we find a duplicate. At each iteration we check to see if the
 * current length substring [i,j) is greater than the max. If we
 * find a duplicate at j, then we keep incrementing i, removing the characters
 * at those indices in the HashSet until the the corresponding duplicate
 * is removed. Repeat until j reaches the end of the string. The max is
 * returned.
 *
 * Each character in the substring is added/removed form the HashSet at most
 * once. If m and n represent the size of the char alphabet and the length of
 * the substring, respectively, then if we used amortized analysis, we have:
 * Time Complexity: O(n)
 * Space Complexity: O(max(m,n))
 */

import java.util.*;


public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<Character>();
        int max = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            while (end < s.length () && !set.contains(s.charAt(end))) {
                end++;
            }
            set.remove(s.charAt(i));
            max = end - i > max ? end - i : max;
        }
        return max;
    }
}
