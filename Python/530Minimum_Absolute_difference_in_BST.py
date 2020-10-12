# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    pre_value = -1
    differences = 2**31 - 1

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.differences

    def dfs(self, root: TreeNode):
        if root is None:
            return

        self.dfs(root.left)

        if self.pre_value == -1:
            self.pre_value = root.val
        else:
            self.differences = min(self.differences, root.val - self.pre_value)
            self.pre_value = root.val

        self.dfs(root.right)


if __name__ == '__main__':
    tree2 = TreeNode(2)
    tree3 = TreeNode(5)
    tree1 = TreeNode(0)
    tree1.right = tree3
    tree3.left = tree2

    solution = Solution()
    print(solution.getMinimumDifference(tree1))

