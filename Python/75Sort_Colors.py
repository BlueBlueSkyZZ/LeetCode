from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        one_index = -1
        two_index = -1

        for i in range(len(nums)):

            if nums[i] == 0:
                if zero_index < 0:
                    zero_index = i
                if one_index >= 0 and i > one_index:
                    swap(nums, i, one_index)
                    if zero_index == i:
                        zero_index = one_index
                    one_index += 1
                elif one_index < 0 and two_index >= 0 and i > two_index:
                    swap(nums, i, two_index)
                    if zero_index == i:
                        zero_index = two_index
                    two_index += 1

            elif nums[i] == 1 and i > two_index:
                if one_index < 0:
                    one_index = i
                if two_index >= 0 and i > two_index:
                    swap(nums, i, two_index)
                    if one_index == i:
                        one_index = two_index
                    two_index += 1
            else:
                if two_index < 0:
                    two_index = i

        if nums[len(nums) - 1] == 1 and two_index >= 0:
            swap(nums, len(nums)-1 , two_index)
        print(nums)

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        index_two = len(nums) - 1

        index_pointer = 0

        while index_zero <= index_two and index_pointer <= index_two:
            if nums[index_pointer] == 0 and index_zero != index_pointer:
                swap(nums, index_zero, index_pointer)
                index_zero += 1
            elif nums[index_pointer] == 2 and index_two != index_pointer:
                swap(nums, index_two, index_pointer)
                index_two -= 1
            else:
                index_pointer += 1
        print(nums)


def swap(nums, index_i, index_j):
    temp = nums[index_i]
    nums[index_i] = nums[index_j]
    nums[index_j] = temp


if __name__ == '__main__':
    nums = [1,2,2,2,2,0,0,0,1,1]
    solution = Solution()
    solution.sortColors(nums)
    solution.sortColors2(nums)