# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # calculate depth
        depth = 0
        temp_root = root
        while temp_root.left is not None:
            depth += 1
            temp_root = temp_root.left

        low, high = 1 << depth, (1 << (depth+1)) - 1

        while low < high:
            mid = (high - low + 1) // 2 + low
            if self.judge_exist(root, depth, mid):
                low = mid
            else:
                high = mid - 1
        return low


    def judge_exist(self, root: TreeNode, depth: int, k: int) -> bool:
        bits = 1 << (depth - 1)
        temp = root
        while temp is not None and bits > 0:
            if bits & k == 0:
                temp = temp.left
            else:
                temp = temp.right
            bits = bits >> 1
        return temp is not None
