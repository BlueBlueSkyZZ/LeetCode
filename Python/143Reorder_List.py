# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        l1 = head

        mid = self.findMiddle(head)
        l2 = mid.next
        # avoid cycle
        mid.next = None

        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def findMiddle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        pre_node = None
        curr_node = head
        while curr_node is not None:
            temp_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = temp_node
        return pre_node

    def mergeList(self, l1: ListNode, l2: ListNode):

        while l1 is not None and l2 is not None:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l2.next = l1_temp

            l1 = l1_temp
            l2 = l2_temp


if __name__ == '__main__':
    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()
    solution.reorderList(node1)

