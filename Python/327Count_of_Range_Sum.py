from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        dp = 0
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                dp = nums[i] if i == j else dp + nums[j]
                if lower <= dp <= upper:
                    result += 1
        return result


if __name__ == '__main__':
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    solution = Solution()
    print(solution.countRangeSum(nums, lower, upper))

