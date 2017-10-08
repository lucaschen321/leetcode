/*
 * Solution to LeetCode Problem 40
 * Source: https://leetcode.com/problems/combination-sum-ii/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a collection of candidate numbers (C) and a target number (T), find all
 * unique combinations in C where the candidate numbers sums to T.
 *
 * Each number in C may only be used once in the combination.
 *
 * Note:
 *
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 *
 *
 *
 * For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
 * A solution set is:
 * [
 *   [1, 7],
 *   [1, 2, 5],
 *   [2, 6],
 *   [1, 1, 6]
 * ]
 */

import java.util.*;

public class CombinationSumII {
     public static List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<Integer> candidateList = new ArrayList<Integer>();
        for (int i = 0; i < candidates.length; i++) {
            candidateList.add(candidates[i]);
        }

        List<List<Integer>> combinations = new ArrayList<List<Integer>>();
        combinationsRecursive(candidateList, target, 0, new ArrayList<Integer>(), combinations);
        return combinations;
    }

    public static void combinationsRecursive (List<Integer> candidates, int target, int candidatesStart, List<Integer> prefix, List<List<Integer>> combinations) {
        for (int i = candidatesStart; i < candidates.size(); i++) {
            if (target == candidates.get(i)) {
                prefix.add(candidates.get(i));
                combinations.add(new ArrayList<>(prefix));
                prefix.remove(prefix.size() - 1);
            }
            if (target > candidates.get(i)) {
                prefix.add(candidates.get(i));
                combinationsRecursive(candidates, target - candidates.get(i), i + 1, prefix, combinations);
                prefix.remove(prefix.size() - 1);
            }
            while (i + 1 < candidates.size() && candidates.get(i) == candidates.get(i + 1)) {
                i++;
            }
        }

    }

    // public static void main(String[] args) {
    //     int[] candidates = {10, 1, -2, -7, 6, -1, 5, -3, 3};
    //     int target = -3;
    //     List<List<Integer>> combinations = combinationSum2(candidates, target);
    //     System.out.println("[");
    //     for (List<Integer> list : combinations) {
    //         String s  = "";
    //         s += "[";
    //         for (Integer i : list) {
    //             s += i + ", ";
    //         }
    //         s = s.substring(0, s.length() - 2) + "],";
    //         System.out.println(s);
    //     }
    //     System.out.println("]");
    // }


}
