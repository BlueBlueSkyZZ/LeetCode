# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, root: TreeNode, parent):
        now_sum = parent * 10 + root.val
        if root.left is not None:
            self.dfs(root.left, now_sum)
        if root.right is not None:
            self.dfs(root.right, now_sum)
        if root.left is None and root.right is None:
            self.sum += now_sum
            return
