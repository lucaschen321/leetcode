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
|1|[Two Sum](https://leetcode.com/problems/two-sum)|  [Java](./java/TwoSum.java), [Python](./python/p0001-two-sum/p0001-two-sum.py)|Array, Hash Table|Easy|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers)| [Java](./java/AddTwoNumbers.java), [Python](./python/p0002-add-two-numbers/p0002-add-two-numbers.py)|Linked List, Math|Medium|
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)|[Java](./java/LongestSubstringWithoutRepeatingCharacters.java), [Python](./python/p0003-longest-substring-without-repeating-characters/p0003-longest-substring-without-repeating-characters.py)|Hash Table, Two Pointers, String, Sliding Window|Medium|
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)|[Java](./java/LongestPalindromicSubstring.java)|String|Medium|
|6|[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion)|[Java](./java/ZigZagConversion.java)|String|Medium|
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer)|[Java](./java/ReverseInteger.java)|Math|Easy|
|9|[Palindrome Number](https://leetcode.com/problems/palindrome-number)|[Java](./java/PalindromeNumber.java)|Math|Easy|
|11|[Container With Most Water](https://leetcode.com/problems/container-with-most-water)|[Java](./java/ContainerWithMostWater.java), [Python](./python/p0011-container-with-most-water/p0011-container-with-most-water.py)|Array, Two Pointers|Medium|
|14|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)|[Java](./java/LongestCommonPrefix.java)|String|Easy|
|15|[3Sum](https://leetcode.com/problems/3sum)|[Java](./java/ThreeSum.java), [Python](./python/p0015-3sum/p0015-3sum.py)|Array, Two Pointers|Medium|
|16|[3Sum Closest](https://leetcode.com/problems/3sum-closest)|[Java](./java/ThreeSumClosest.java)|Array, Two Pointers|Medium|
|17|[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)|[Java](./java/LetterCombinationsofaPhoneNumber.java), [Python](./python/p0017-letter-combinations-of-a-phone-number/p0017-letter-combinations-of-a-phone-number.py)|String, Backtracking|Medium|
|18|[4Sum](https://leetcode.com/problems/4sum)|[Java](./java/FourSum.java)|Array, Hash Table, Two Pointers|Medium|
|19|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)|[Java](./java/RemoveNthNodeFromEndofList.java), [Python](./python/p0019-remove-nth-node-from-end-of-list/p0019-remove-nth-node-from-end-of-list.py)|Linked List, Two Pointers|Medium|
|20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses)|[Python](./python/p0020-valid-parentheses/p0020-valid-parentheses.py)|String, Stack|Easy|
|21|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)|[Java](./java/MergeTwoSortedLists.java)|Linked List|Easy|
|22|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses)|[Java](./java/GenerateParentheses.java)|String, Backtracking|Medium|
|23|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)|[Java](./java/MergekSortedLists.java), [Python](./python/p0023-merge-k-sorted-lists/p0023-merge-k-sorted-lists.py)|Linked List, Divide and Conquer, Heap|Hard|
|24|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs)|[Java](./java/SwapNodesinPairs.java)|Linked List|Medium|
|26|[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)|[C++](./c++/RemoveDuplicatesfromSortedArray.cpp), [Python](./python/p0026-remove-duplicates-from-sorted-array/p0026-remove-duplicates-from-sorted-array.py)|Array, Two Pointers|Easy|
|31|[Next Permutation](https://leetcode.com/problems/next-permutation)|[C++](./c++/NextPermutation.cpp)|Array|Medium|
|33|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array)|[Python](./python/p0033-search-in-rotated-sorted-array/p0033-search-in-rotated-sorted-array.py)|Array, Binary Search|Medium|
|34|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)|[Python](./python/p0034-find-first-and-last-position-of-element-in-sorted-array/p0034-find-first-and-last-position-of-element-in-sorted-array.py)|Array, Binary Search|Medium|
|36|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku)|[Python](./python/p0036-valid-sudoku/p0036-valid-sudoku.py)|Hash Table|Medium|
|39|[Combination Sum](https://leetcode.com/problems/combination-sum)|[Java](./java/CombinationSum.java), [Python](./python/p0039-combination-sum/p0039-combination-sum.py)|Array, Backtracking|Medium|
|40|[Combination Sum II](https://leetcode.com/problems/combination-sum-ii)|[Java](./java/CombinationSumII.java)|Array, Backtracking|Medium|
|42|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)|[C++](./c++/TrappingRainWater.cpp), [Python](./python/p0042-trapping-rain-water/p0042-trapping-rain-water.py)|Array, Two Pointers, Stack|Hard|
|48|[Rotate Image](https://leetcode.com/problems/rotate-image)|[Python](./python/p0048-rotate-image/p0048-rotate-image.py)|Array|Medium|
|49|[Group Anagrams](https://leetcode.com/problems/group-anagrams)|[Python](./python/p0049-group-anagrams/p0049-group-anagrams.py)|Hash Table, String|Medium|
|51|[N-Queens](https://leetcode.com/problems/n-queens)|[C++](./c++/N-Queens.cpp)|Backtracking|Hard|
|53|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray)|[Python](./python/p0053-maximum-subarray/p0053-maximum-subarray.py)|Array, Divide and Conquer, Dynamic Programming|Easy|
|56|[Merge Intervals](https://leetcode.com/problems/merge-intervals)|[C++](./c++/MergeIntervals.cpp), [Python](./python/p0056-merge-intervals/p0056-merge-intervals.py)|Array, Sort|Medium|
|62|[Unique Paths](https://leetcode.com/problems/unique-paths)|[Python](./python/p0062-unique-paths/p0062-unique-paths.py)|Array, Dynamic Programming|Medium|
|72|[Edit Distance](https://leetcode.com/problems/edit-distance)|[C++](./c++/EditDistance.cpp)|String, Dynamic Programming|Hard|
|76|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)|[C++](./c++/MinimumWindowSubstring.cpp), [Python](./python/p0076-minimum-window-substring/p0076-minimum-window-substring.py)|Hash Table, Two Pointers, String, Sliding Window|Hard|
|78|[Subsets](https://leetcode.com/problems/subsets)|[Python](./python/p0078-subsets/p0078-subsets.py)|Array, Backtracking, Bit Manipulation|Medium|
|98|[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)|[Python](./python/p0098-validate-binary-search-tree/p0098-validate-binary-search-tree.py)|Tree, Depth-first Search|Medium|
|102|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|[C++](./c++/BinaryTreeLevelOrderTraversal.cpp), [Java](./java/BinaryTreeLevelOrderTraversal.java)|Tree, Breadth-first Search|Medium|
|103|[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)|[Python](./python/p0103-binary-tree-zigzag-level-order-traversal/p0103-binary-tree-zigzag-level-order-traversal.py)|Stack, Tree, Breadth-first Search|Medium|
|105|[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)|[Python](./python/p0105-construct-binary-tree-from-preorder-and-inorder-traversal/p0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)|Array, Tree, Depth-first Search|Medium|
|121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)|[Java](./java/BestTimetoBuyandSellStock.java)|Array, Dynamic Programming|Easy|
|122|[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)|[Java](./java/BestTimetoBuyandSellStockII.java)|Array, Greedy|Easy|
|124|[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)|[Python](./python/p0124-binary-tree-maximum-path-sum/p0124-binary-tree-maximum-path-sum.py)|Tree, Depth-first Search|Hard|
|133|[Clone Graph](https://leetcode.com/problems/clone-graph)|[Python](./python/p0133-clone-graph/p0133-clone-graph.py)|Depth-first Search, Breadth-first Search, Graph|Medium|
|139|[Word Break](https://leetcode.com/problems/word-break)|[C++](./c++/WordBreak.cpp), [Java](./java/WordBreak.java) |Dynamic Programming|Medium|
|141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)|[Python](./python/p0141-linked-list-cycle/p0141-linked-list-cycle.py)|Linked List, Two Pointers|Easy|
|152|[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray)|[Python](./python/p0152-maximum-product-subarray/p0152-maximum-product-subarray.py)|Array, Dynamic Programming|Medium|
|153|[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)|[Python](./python/p0153-find-minimum-in-rotated-sorted-array/p0153-find-minimum-in-rotated-sorted-array.py)|Array, Binary Search|Medium|
|154|[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii)|[Python](./python/p0154-find-minimum-in-rotated-sorted-array-ii/p0154-find-minimum-in-rotated-sorted-array-ii.py)|Array, Binary Search|Hard|
|200|[Number of Islands](https://leetcode.com/problems/number-of-islands)|[Python](./python/p0200-number-of-islands/p0200-number-of-islands.py)|Depth-first Search, Breadth-first Search, Union Find|Medium|
|206|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)|[Python](./python/p0206-reverse-linked-list/p0206-reverse-linked-list.py)|Linked List|Easy|
|207|[Course Schedule](https://leetcode.com/problems/course-schedule)|[Python](./python/p0207-course-schedule/p0207-course-schedule.py)|Depth-first Search, Breadth-first Search, Graph, Topological Sort|Medium|
|210|[Course Schedule II](https://leetcode.com/problems/course-schedule-ii)|[Python](./python/p0210-course-schedule-ii/p0210-course-schedule-ii.py)|Depth-first Search, Breadth-first Search, Graph, Topological Sort|Medium|
|218|[The Skyline Problem](https://leetcode.com/problems/the-skyline-problem)|[Python](./python/p0218-the-skyline-problem/p0218-the-skyline-problem.py)|Divide and Conquer, Heap, Binary Indexed Tree, Segment Tree, Line Sweep|Hard|
|224|[Basic Calculator](https://leetcode.com/problems/basic-calculator)|[Python](./python/p0224-basic-calculator/p0224-basic-calculator.py)|Math, Stack|Hard|
|226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree)|[Python](./python/p0226-invert-binary-tree/p0226-invert-binary-tree.py)|Tree|Easy|
|230|[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)|[Python](./python/p0230-kth-smallest-element-in-a-bst/p0230-kth-smallest-element-in-a-bst.py)|Binary Search, Tree|Medium|
|238|[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)|[Python](./python/p0238-product-of-array-except-self/p0238-product-of-array-except-self.py)|Array|Medium|
|274|[H-Index](https://leetcode.com/problems/h-index)|[Python](./python/p0274-h-index/p0274-h-index.py)|Hash Table, Sort|Medium|
|275|[H-Index II](https://leetcode.com/problems/h-index-ii)|[Python](./python/p0275-h-index-ii/p0275-h-index-ii.py)|Binary Search|Medium|
|297|[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)|[Python](./python/p0297-serialize-and-deserialize-binary-tree/p0297-serialize-and-deserialize-binary-tree.py)|Tree, Design|Hard|
|301|[Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)|[Python](./python/p0301-remove-invalid-parentheses/p0301-remove-invalid-parentheses.py)|Depth-first Search, Breadth-first Search|Hard|
|347|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)|[Python](./python/p0347-top-k-frequent-elements/p0347-top-k-frequent-elements.py)|Hash Table, Heap|Medium|
|417|[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow)|[Python](./python/p0417-pacific-atlantic-water-flow/p0417-pacific-atlantic-water-flow.py)|Depth-first Search, Breadth-first Search|Medium|
|424|[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)|[Python](./python/p0424-longest-repeating-character-replacement/p0424-longest-repeating-character-replacement.py)|Two Pointers, Sliding Window|Medium|
|435|[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals)|[Python](./python/p0435-non-overlapping-intervals/p0435-non-overlapping-intervals.py)|Greedy|Medium|
|647|[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings)|[Python](./python/p0647-palindromic-substrings/p0647-palindromic-substrings.py)|String, Dynamic Programming|Medium|
