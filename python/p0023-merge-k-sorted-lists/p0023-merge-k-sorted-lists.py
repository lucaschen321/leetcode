from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1: Merge lists using a heap of size k, with elements from each list.
class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = [(element.val, i, element.next) for i, element in enumerate(lists) if element]
        heapq.heapify(min_heap)
        dummy_node = curr_node = ListNode(0)
        while (min_heap):
            min_node_val, i, min_node_next = heapq.heappop(min_heap)
            if min_node_next:
                heapq.heappush(min_heap, (min_node_next.val, i, min_node_next.next))
            curr_node.next = ListNode(min_node_val)
            curr_node = curr_node.next

        return dummy_node.next


# Solution 2: Use divide-and-conquer. The result of merging k lists is the same as
# merging each half of size k/2 lists, then combining them, and so on recursively.
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(list1, list2) -> ListNode:
            dummy = current = ListNode(0)
            while (list1 and list2):
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 if list1 else list2
            return dummy.next

        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return merge2Lists(left, right)
