# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# < 4096 == 2 ** 12
class Solution:

    def connect(self, root: 'Node') -> 'Node':
        self.subconnect(root)
        return root

    def subconnect(self, root):
        if root is None:
            return
        if root.left is not None:
            root.left.next = root.right
        if root.next is not None and root.right is not None:
            root.right.next = root.next.left

        self.subconnect(root.left)
        self.subconnect(root.right)


