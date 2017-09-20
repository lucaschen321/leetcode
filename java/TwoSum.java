/*
 * Solution to Leetcode Problem 1
 * Source: https://leetcode.com/problems/two-sum/
 * Author: Lucas Chen
 */

/*
 * We can make one pass through the array, iterating and inserting elements
 * into the hashtable, while checking if the current element's complement
 * to the target exists in the table. If the complement exists, we are finished
 * and we can return a solution.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement))
                return new int[]{map.get(complement), i};
            else
                map.put(nums[i], i);
        }
        return new int[]{0, 0};
    }
}
