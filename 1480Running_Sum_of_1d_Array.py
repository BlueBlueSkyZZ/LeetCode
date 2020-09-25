from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        简单的累加
        :param nums:
        :return:
        """
        for i in range(len(nums)-1):
            nums[i+1] = nums[i+1] + nums[i]
        return nums


if __name__ == '__main__':
    nums = [3, 1, 2, 10, 1]
    solution = Solution()
    print(solution.runningSum(nums))

