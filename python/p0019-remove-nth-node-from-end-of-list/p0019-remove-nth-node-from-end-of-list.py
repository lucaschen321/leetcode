# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = left = right = ListNode(0)
        left.next = head

        for i in range(n + 1):
            right = right.next

        while right:
            left, right = left.next, right.next

        # left points to (k + 1)-th last node, delete its successor
        left.next = left.next.next

        return dummy.next
