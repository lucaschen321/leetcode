/*
 * Solution to Leetcode Problem 2
 * Source: https://leetcode.com/problems/add-two-numbers/
 * Author: Lucas Chen
 */

/*
 * Converting the lists to numbers, adding them, and converting the sum back to
 * a linked list would require a BigInteger import to avoid integer overflow
 * if built-in types were used. Such an algorithm would likely have overhead
 * from BigInteger operations, so a manual algorithm with bit by bit addition
 * is chosen instead. A carry-in bit is used. To take care of the case when the
 * length of l1 and l2 are different lengths, we set the "value" added as 0
 * if we reach the end of one of them. Iteration occurs until the end of both
 * lists is reached and the carry bit is 0. A dummy head is also used to avoid
 * having to repeat loop body logic to initialize the head.
 *
 * If m and n represent the length of lists [l1] and [l2], respectively, then:
 * Time Complexity: O(max(m,n))
 * Space Complexity: O(max(m,n))
 */


public class AddTwoNumbers {
    /**
     *  Definition for singly-linked list.
     */
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l_dummy = new ListNode(0);
        ListNode l_sum = l_dummy;
        int carry = 0;
        int l1_val, l2_val, l_sum_bits, l_sum_bits_val;

        while (l1 != null || l2 != null || carry == 1) {
            if (l1 == null)
                l1_val = 0;
            else {
                l1_val = l1.val;
                l1 = l1.next;
            }

            if (l2 == null)
                l2_val = 0;
            else {
                l2_val = l2.val;
                l2 = l2.next;
            }

            l_sum_bits = l1_val + l2_val + carry;
            l_sum_bits_val = l_sum_bits % 10;
            carry = l_sum_bits / 10;

            l_sum.next = new ListNode(l_sum_bits_val);
            l_sum = l_sum.next;
        }

        return l_dummy.next;
    }
}
