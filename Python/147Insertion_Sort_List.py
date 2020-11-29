# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        sorted_end = head
        now_pointer = head.next
        while now_pointer is not None:
            temp_pointer = now_pointer
            if now_pointer.val >= sorted_end.val:
                sorted_end = now_pointer
            else:
                pre_pointer = head
                curr_pointer = head
                while curr_pointer is not None:  # insert sort
                    if curr_pointer.val < now_pointer.val:  # is not the right insert position
                        pre_pointer = curr_pointer
                        curr_pointer = curr_pointer.next
                    else:  # need to insert between pre and curr
                        if pre_pointer == curr_pointer:  # insert to head
                            sorted_end.next = now_pointer.next
                            now_pointer.next = head
                            head = now_pointer
                        else:
                            sorted_end.next = now_pointer.next
                            pre_pointer.next = now_pointer
                            now_pointer.next = curr_pointer
                        sorted_end = curr_pointer
                        break

            now_pointer = temp_pointer.next

        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node2.next = node1
    node3 = ListNode(2)
    node3.next = node2
    node4 = ListNode(4)
    node4.next = node3

    head = node4
    solution = Solution()
    solution.insertionSortList(head)
