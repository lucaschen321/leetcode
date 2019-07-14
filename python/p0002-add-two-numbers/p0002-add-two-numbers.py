# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Get l1 to int
        l1_str = str(l1.val)
        while (l1.next):
            l1 = l1.next
            l1_str = str(l1.val) + l1_str

        # Get l2 to int
        l2_str = str(l2.val)
        while (l2.next):
            l2 = l2.next
            l2_str = str(l2.val) + l2_str

        l_ans_str = str(int(l1_str) + int(l2_str))
        l_ans = ListNode(l_ans_str[-1])
        head = l_ans
        for i in range(len(l_ans_str) - 1):
            l_ans.next = ListNode(l_ans_str[::-1][i + 1])
            l_ans = l_ans.next

        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_ptr = curr_ptr = ListNode(0)
        carry = 0

        while (l1 or l2 or carry):
            curr_val = 0
            if (l1):
                curr_val += l1.val
                l1 = l1.next
            if (l2):
                curr_val += l2.val
                l2 = l2.next

            curr_val += carry
            carry = curr_val // 10
            curr_ptr.next = ListNode(curr_val % 10)
            curr_ptr = curr_ptr.next

        return head_ptr.next
