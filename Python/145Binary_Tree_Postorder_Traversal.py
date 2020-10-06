# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        result = []

        def recursion(root: TreeNode):
            if root is None:
                return None
            recursion(root.left)
            recursion(root.right)
            result.append(root.val)

        recursion(root)

        return result


if __name__ == '__main__':
    left3 = TreeNode(3, None, None)
    right2 = TreeNode(2, left3, None)
    root1 = TreeNode(1, None, right2)

    solution = Solution()
    print(solution.postorderTraversal(root1))