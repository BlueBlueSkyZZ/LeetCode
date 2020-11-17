from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums: List[int], i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverse(nums: List[int], start):
            nums_len = len(nums)
            for i in range(start, (start+nums_len-1)//2 + 1):
                swap(nums, i, nums_len-1+start-i)

        nums_len = len(nums)
        small_index = 0
        big_index = nums_len-1
        exchange_flag = False

        # find small index
        for i in range(nums_len-2, -1, -1):
            if nums[i+1] > nums[i]:
                small_index = i
                exchange_flag = True
                break

        # find big index
        for i in range(nums_len-1, small_index, -1):
            if nums[i] > nums[small_index]:
                big_index = i
                exchange_flag = True
                break
        if exchange_flag is True:
            swap(nums, small_index, big_index)
            reverse(nums, small_index+1)
        else:
            reverse(nums, 0)
        print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 8, 5, 7, 6, 4]
    nums = [2,3,1]
    solution = Solution()
    solution.nextPermutation(nums)
