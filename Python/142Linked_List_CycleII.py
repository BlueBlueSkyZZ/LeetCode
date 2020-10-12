# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        slow_pointer = head.next
        fast_pointer = head.next.next

        while slow_pointer != fast_pointer:
            if fast_pointer is None or fast_pointer.next is None:
                return None
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        fast_pointer = head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer

