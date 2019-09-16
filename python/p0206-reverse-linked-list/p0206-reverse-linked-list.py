# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Iterative solution.
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        previous, current = None, head
        while current:
            current.next, previous, current = previous, current, current.next

        return previous


# Solution 2: Recursive solution.
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # List is empty or at end of list
            return head
        else:
            rest = self.reverseList(head.next)  # rest is always last node in original list
            head.next.next = head
            head.next = None
            return rest
