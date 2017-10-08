/*
 * Solution to LeetCode Problem 19
 * Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Given a linked list, remove the nth node from the end of list and return its
 * head.
 *
 * For example,
 *    Given linked list: 1->2->3->4->5, and n = 2.
 *
 *    After removing the second node from the end, the linked list becomes
 * 1->2->3->5.
 *
 *
 * Note:
 * Given n will always be valid.
 * Try to do this in one pass.
 */

import java.util.*;

public class RemoveNthNodeFromEndofList {

    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

     public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode leader = dummyHead, trailing = dummyHead;
        for (int i = 0; i < n; i++) {
            leader = leader.next;
        }

        while (leader.next != null) {
            trailing = trailing.next;
            leader = leader.next;
        }

        trailing.next = trailing.next.next;
        return dummyHead.next;
    }
}
