# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashset = set()
        while head is not None:
            if head in hashset:
                return True
            hashset.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slower_pointer = head
        faster_pointer = head.next

        while slower_pointer != faster_pointer:
            if faster_pointer is None or faster_pointer.next is None:
                return False
            slower_pointer = slower_pointer.next
            faster_pointer = faster_pointer.next.next

        return True