/*
 * Solution to LeetCode Problem 39
 * Source: https://leetcode.com/problems/combination-sum/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a set of candidate numbers (C) (without duplicates) and a target number
 * (T), find all unique combinations in C where the candidate numbers sums to T.
 *
 * The same repeated number may be chosen from C unlimited number of times.
 *
 * Note:
 *
 * All numbers (including target) will be positive integers.
 * The solution set must not contain duplicate combinations.
 *
 *
 *
 * For example, given candidate set [2, 3, 6, 7] and target 7,
 * A solution set is:
 * [
 *   [7],
 *   [2, 2, 3]
 * ]
 */

import java.util.*;

public class CombinationSum {
     public static List<List<Integer>> combinationSum(int[] candidates, int target) {
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
                combinationsRecursive(candidates, target - candidates.get(i), i, prefix, combinations);
                prefix.remove(prefix.size() - 1);
            }
        }

    }
    // public static void main(String[] args) {
    //     int[] candidates = {2, 3, 6, 7};
    //     int target = 7;
    //     List<List<Integer>> combinations = combinationSum(candidates, target);
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
