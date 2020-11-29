from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i-zero_count] = nums[i]

        if zero_count > 0:
            nums[-zero_count:] = [0] * zero_count

        print(nums)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [1]
    solution = Solution()
    solution.moveZeroes(nums)
