# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(head: ListNode, tail: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            slow_p, fast_p = head, head.next
            while fast_p is not tail and fast_p is not None and fast_p.next is not None:
                slow_p = slow_p.next
                fast_p = fast_p.next.next
            mid_p = slow_p.next
            slow_p.next = None

            return merge(mergeSort(head, slow_p), mergeSort(mid_p, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummy_head = ListNode(0)

            pointer = dummy_head
            pointer1 = head1
            pointer2 = head2

            while pointer1 is not None and pointer2 is not None:
                if pointer1.val <= pointer2.val:
                    pointer.next = pointer1
                    pointer1 = pointer1.next
                else:
                    pointer.next = pointer2
                    pointer2 = pointer2.next
                pointer = pointer.next

            if pointer1 is not None:
                pointer.next = pointer1
            elif pointer2 is not None:
                pointer.next = pointer2

            return dummy_head.next

        return mergeSort(head, None)

if __name__ == '__main__':
    node0 = ListNode(0)
    node1 = ListNode(4)
    node1.next = node0
    node2 = ListNode(3)
    node2.next = node1
    node3 = ListNode(5)
    node3.next = node2
    node4 = ListNode(-1)
    node4.next = node3

    head = node4
    solution = Solution()
    solution.sortList(head)