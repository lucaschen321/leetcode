# LeetCode

## Scripts

`add_problem.py` - used to generate author and problem description comments & add the problem to README

> **Notes**:
> - Description and tags are parsed from LeetCode's HTML DOM using BeautifulSoup
> - Comments and description are 80 character aligned

### Usage

1. Create a file named TwoSum.java and add comments & problem description.

    `./add_problem.py https://leetcode.com/problems/two-sum`

2. Prompts for whether to create file (created in `/java/`) and whether to add to `README`

The comments generated by the example above as below:

```java

/*
 * Solution to LeetCode Problem 1
 * Source: https://leetcode.com/problems/two-sum
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given an array of integers, return indices of the two numbers such that they add
 * up to a specific target.
 * You may assume that each input would have exactly one solution, and you may not
 * use the same element twice.
 *
 * Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 *
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 */

import java.util.*;

public class TwoSum {

}
```

## Problems
<!---anchor--->
| # | Title | Solution | Tags | Difficulty |
|---| ----- | -------- | -----| ---------- |
|1|[Two Sum](https://leetcode.com/problems/two-sum)|  [Java](./java/TwoSum.java), [Python](./python/p0001-two-sum/p0001-two-sum.py)|Array Hash Table|Easy|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers)| [Java](./java/AddTwoNumbers.java), [Python](./python/p0002-add-two-numbers/p0002-add-two-numbers.py)|Linked List Math|Medium|
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)| [Java](./java/LongestSubstringWithoutRepeatingCharacters.java), [Python](./python/p0003-longest-substring-without-repeating-characters/p0003-longest-substring-without-repeating-characters.py)|Medium|
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)|[Java](./java/LongestPalindromicSubstring.java)|String|Medium|
|6|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion)|[Java](./java/ZigZagConversion.java)|String|Medium|
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer)|[Java](./java/ReverseInteger.java)|Math|Easy|
|9|[Palindrome Number](https://leetcode.com/problems/palindrome-number)|[Java](./java/PalindromeNumber.java)|Math|Easy|
|11|[Container With Most Water](https://leetcode.com/problems/container-with-most-water)|[Java](./java/ContainerWithMostWater.java)|Array, Two Pointers|Medium|
|14|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)|[Java](./java/LongestCommonPrefix.java)|String|Easy|
|15|[3Sum](https://leetcode.com/problems/3sum)|[Java](./java/ThreeSum.java)|Array, Two Pointers|Medium|
|16|[3Sum Closest](https://leetcode.com/problems/3sum-closest)|[Java](./java/ThreeSumClosest.java)|Array, Two Pointers|Medium|
|17|[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)|[Java](./java/LetterCombinationsofaPhoneNumber.java)|String, Backtracking|Medium|
|18|[4Sum](https://leetcode.com/problems/4sum)|[Java](./java/FourSum.java)|Array, Hash Table, Two Pointers|Medium|
|19|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)|[Java](./java/RemoveNthNodeFromEndofList.java)|Linked List, Two Pointers|Medium|
|21|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)|[Java](./java/MergeTwoSortedLists.java)|Linked List|Easy|
|22|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses)|[Java](./java/GenerateParentheses.java)|String, Backtracking|Medium|
|23|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)|[Java](./java/MergekSortedLists.java)|Linked List, Divide and Conquer, Heap|Hard|
|24|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)|[Java](./java/SwapNodesinPairs.java)|Linked List|Medium|
|26|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)|[C++](./c++/RemoveDuplicatesfromSortedArray.cpp), [Python](./python/p0026-remove-duplicates-from-sorted-array/p0026-remove-duplicates-from-sorted-array.py)|Array Two Pointers|Easy|
|31|[Next Permutation](https://leetcode.com/problems/next-permutation)|[C++](./c++/NextPermutation.cpp)|Array|Medium|
|34|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)|[Python](./python/p0034-find-first-and-last-position-of-element-in-sorted-array/p0034-find-first-and-last-position-of-element-in-sorted-array.py)|Array Binary Search|Medium|
|39|[Combination Sum](https://leetcode.com/problems/combination-sum)|[Java](./java/CombinationSum.java)|Array, Backtracking|Medium|
|40|[Combination Sum II](https://leetcode.com/problems/combination-sum-ii)|[Java](./java/CombinationSumII.java)|Array, Backtracking|Medium|
|42|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)|[C++](./c++/TrappingRainWater.cpp)|ArrayTwo PointersStack|Hard|
|51|[N-Queens](https://leetcode.com/problems/n-queens)|[C++](./c++/N-Queens.cpp)|Backtracking|Hard|
|56|[Merge Intervals](https://leetcode.com/problems/merge-intervals)|[C++](./c++/MergeIntervals.cpp), [Python](./python/p0056-merge-intervals/p0056-merge-intervals.py)|Array Sort|Medium|
|72|[Edit Distance](https://leetcode.com/problems/edit-distance)|[C++](./c++/EditDistance.cpp)|StringDynamic Programming|Hard|
|76|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)|[C++](./c++/MinimumWindowSubstring.cpp)|Hash TableTwo PointersString|Hard|
|102|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|[C++](./c++/BinaryTreeLevelOrderTraversal.cpp), [Java](./java/BinaryTreeLevelOrderTraversal.java)|TreeBreadth-first Search|Medium|
|121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)|[Java](./java/BestTimetoBuyandSellStock.java)|Array, Dynamic Programming|Easy|
|122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)|[Java](./java/BestTimetoBuyandSellStockII.java)|Array, Greedy|Easy|
|139|[Word Break](https://leetcode.com/problems/word-break)|[C++](./c++/WordBreak.cpp), [Java](./java/WordBreak.java)|Dynamic Programming|Medium|
