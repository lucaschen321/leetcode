#include "leetcode.h"

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode l_dummy = ListNode(0);
        ListNode* l_sum = &l_dummy;
        int carry = 0;
        int l1_val, l2_val, l_sum_bits, l_sum_bits_val;

        while (l1 != NULL || l2 != NULL || carry == 1) {
            if (l1 == NULL)
                l1_val = 0;
            else {
                l1_val = l1 -> val;
                l1 = l1 -> next;
            }

            if (l2 == NULL)
                l2_val = 0;
            else {
                l2_val = l2 -> val;
                l2 = l2 -> next;
            }

            l_sum_bits = l1_val + l2_val + carry;
            l_sum_bits_val = l_sum_bits % 10;
            carry = l_sum_bits / 10;

            l_sum->next = new ListNode(l_sum_bits_val);
            l_sum = l_sum->next;
        }

        return l_dummy.next;


    }
};
