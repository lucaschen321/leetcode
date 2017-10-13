/*
 * Solution to LeetCode Problem 21
 * Source: https://leetcode.com/problems/merge-two-sorted-lists/description/
 * Author: Lucas Chen
 */

/*
 * Description:
 * Merge two sorted linked lists and return it as a new list. The new list should
 * be made by splicing together the nodes of the first two lists.
 */

import java.util.*;

public class MergeTwoSortedLists {

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }


    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        ListNode mergeHead;
        if (l1.val < l2.val) {
            mergeHead = l1;
            mergeHead.next = mergeTwoLists(l1.next, l2);
        }
        else {
            mergeHead = l2;
            mergeHead.next = mergeTwoLists(l1, l2.next);
        }
        return mergeHead;
    }

   // public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
   //          ListNode dummy = new ListNode(0);
   //          ListNode minNode = dummy;
   //          if (l1 == null) {
   //              return l2;
   //          }
   //          if (l2 == null) {
   //              return l1;
   //          }
   //
   //
   //          if (l1.val < l2.val ) {
   //              dummy.next = l1;
   //          }
   //          else {
   //              dummy.next = l2;
   //          }
   //
   //          while (l1 != null || l2 != null) {
   //              if (l2 == null && l1 != null) {
   //                  minNode.next = l1;
   //                  l1 = l1.next;
   //              } else if (l1 == null && l2 != null) {
   //                  minNode.next = l2;
   //                  l2 = l2.next;
   //              }
   //              else if (l1.val < l2.val) {
   //                  minNode.next = l1;
   //                  l1 = l1.next;
   //              }
   //              else {
   //                  minNode.next = l2;
   //                  l2 = l2.next;
   //              }
   //              minNode = minNode.next;
   //
   //          }
   //          return dummy.next;
   //  }

}
