# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
        # self.printList(head)
        middle_node = self.getMiddle(head)
        new_head = self.reverseList(middle_node.next)
        # self.printList(new_head)
        while new_head is not None:
            if new_head.val == head.val:
                new_head = new_head.next
                head = head.next
            else:
                return False
        return True

    def getMiddle(self, head: ListNode) -> ListNode:
        slow_pointer = head
        fast_pointer = head.next
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

    def reverseList(self, head: ListNode):
        previous_node = None
        while head is not None:
            temp_node = head.next
            head.next = previous_node
            previous_node = head
            head = temp_node
        return previous_node

    def printList(self, head: ListNode) -> None:
        while head is not None:
            print(head.val)
            head = head.next
        print('-------')


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node5 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = node5

    solution = Solution()
    print(solution.isPalindrome(node1))



