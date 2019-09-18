# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tortoise = hare = head

        while hare and hare.next:
            tortoise, hare = tortoise.next, hare.next.next
            if tortoise == hare:
                return True

        return False
