/*
 * Solution to LeetCode Problem 18
 * Source: https://leetcode.com/problems/4sum/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given an array S of n integers, are there elements a, b, c, and d in S such that
 * a + b + c + d = target? Find all unique quadruplets in the array which gives the
 * sum of target.
 * Note: The solution set must not contain duplicate quadruplets.
 *
 * For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
 *
 * A solution set is:
 * [
 *   [-1,  0, 0, 1],
 *   [-2, -1, 1, 2],
 *   [-2,  0, 0, 2]
 * ]
 */

import java.util.*;

public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
            Map<Integer, List<List<Integer>>> map = new HashMap<Integer, List<List<Integer>>>();
            Set<List<Integer>> ans = new HashSet<List<Integer>>();
            for (int i = 0; i < nums.length; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (!map.containsKey(nums[i] + nums[j])) {
                        List<List<Integer>> temp = new ArrayList<List<Integer>>();
                        temp.add(Arrays.asList(i, j));
                        map.put(nums[i] + nums[j], temp);
                    }
                    else {
                        map.get(nums[i] + nums[j]).add(Arrays.asList(i,j));
                    }
                }
            }

            List<Integer> keys = new ArrayList<Integer>(map.keySet());
            Collections.sort(keys);
            int l = 0, r = keys.size() - 1;
            while (l <= r) {
                if (keys.get(l) + keys.get(r) == target) {
                    List<List<Integer>> keyIndicesLeftList  = map.get(keys.get(l));
                    List<List<Integer>> keyIndicesRightList  = map.get(keys.get(r));
                    for (int a = 0; a < keyIndicesLeftList.size(); a++) {
                        for (int b = 0; b < keyIndicesRightList.size(); b++) {
                            boolean unique = true;
                            List<Integer> keyIndicesLeft = keyIndicesLeftList.get(a);
                            List<Integer> keyIndicesRight = keyIndicesRightList.get(b);
                            for (Integer i : keyIndicesLeft) {
                                for (Integer j : keyIndicesRight) {
                                    if (i == j) {
                                        unique = false;
                                    }
                                }
                            }
                            if (unique) {
                                List<Integer> temp = new ArrayList<>();
                                for (Integer i : keyIndicesLeft) {
                                    temp.add(nums[i]);
                                }
                                for (Integer i : keyIndicesRight) {
                                    temp.add(nums[i]);
                                }
                                Collections.sort(temp);
                                ans.add(temp);
                            }

                            }
                        }
                    l++;
                    r--;
                } else if (keys.get(l) + keys.get(r) < target) {
                    l++;
                }
                else {
                    r--;
                }
            }

        return new ArrayList<List<Integer>>(ans);
    }
}
