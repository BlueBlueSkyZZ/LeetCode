# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_pointer = head
        suf_pointer = head
        suf_pointer_last = head

        while n > 0:
            pre_pointer = pre_pointer.next
            n = n - 1

        while pre_pointer is not None:
            pre_pointer = pre_pointer.next
            suf_pointer_last = suf_pointer
            suf_pointer = suf_pointer.next

        # if removed node is head
        if suf_pointer_last == suf_pointer:
            return head.next

        suf_pointer_last.next = suf_pointer.next
        return head

