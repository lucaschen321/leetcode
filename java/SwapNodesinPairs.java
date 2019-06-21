/*
 * Solution to LeetCode Problem 24
 * Source: https://leetcode.com/problems/swap-nodes-in-pairs/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a linked list, swap every two adjacent nodes and return its head.
 *
 *
 * For example,
 * Given 1->2->3->4, you should return the list as 2->1->4->3.
 *
 *
 * Your algorithm should use only constant space. You may not modify the values in
 * the list, only nodes itself can be changed.
 */

import java.util.*;

public class SwapNodesinPairs {
    // Definition for singly-linked list.
     public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
     }

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode trailing = head, leader = trailing.next;
        head = head.next;

        while (leader != null) {
            ListNode next = leader.next;
            if (leader.next == null || leader.next.next == null) {
                leader.next = trailing;
                trailing.next = next;
                break;
            }
            leader.next = trailing;
            trailing.next = next.next;
            leader = next.next;
            trailing = next;
        }

        return head;
    }
}
