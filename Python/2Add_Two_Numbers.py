class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        init_node = None
        last_node = None
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                new_node = ListNode((l1.val + l2.val + carry) % 10)
                carry = 1 if (l1.val + l2.val + carry >= 10) else 0
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None and l2 is None:
                new_node = ListNode((l1.val + carry) % 10)
                carry = 1 if (l1.val + carry >= 10) else 0
                l1 = l1.next
            elif l2 is not None and l1 is None:
                new_node = ListNode((l2.val + carry) % 10)
                carry = 1 if (l2.val + carry >= 10) else 0
                l2 = l2.next

            if init_node is None:
                init_node = new_node
            else:
                last_node.next = new_node
            last_node = new_node
        if carry == 1:
            new_node = ListNode(1)
            last_node.next = new_node

        return init_node


def printList(l1: ListNode):
    while l1 is not None:
        print(l1.val)
        l1 = l1.next


if __name__ == '__main__':
   l1_1 = ListNode(9)
   l1_2 = ListNode(4, l1_1)
   l1_3 = ListNode(2, l1_2)

   l2_1 = ListNode(9)
   l2_2 = ListNode(4, l2_1)
   l2_3 = ListNode(6, l2_2)
   l2_4 = ListNode(5, l2_3)

   solution = Solution()
   printList(solution.addTwoNumbers(l1_3, l2_4))
