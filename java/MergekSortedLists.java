/*
 * Solution to LeetCode Problem 23
 * Source: https://leetcode.com/problems/merge-k-sorted-lists/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 */

import java.util.*;

public class MergekSortedLists {
     // Definition for singly-linked list.
     public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        PriorityQueue<ListNode> heap = new PriorityQueue<>((l1, l2) -> (l1.val - l2.val));

        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;

        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                heap.add(lists[i]);
            }
        }

        while (heap.peek() != null) {
            ListNode removed = heap.peek();
            heap.remove();
            current.next = removed;
            current = current.next;

            if (removed.next != null) {
                heap.add(removed.next);
            }
        }
        return dummyHead.next;
    }
}
