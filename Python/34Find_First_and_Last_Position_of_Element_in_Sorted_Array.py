from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], nums_size: int, target: int, find_lower: bool) -> int:
            left, right, result = 0, nums_size-1, nums_size
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (find_lower and nums[mid] >= target):
                    result = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        left_index = binarySearch(nums, len(nums), target, True)
        right_index = binarySearch(nums, len(nums), target, False) - 1

        if left_index <= right_index and nums[left_index] == target and nums[right_index] == target:
            return [left_index, right_index]
        return [-1, -1]


if __name__ == '__main__':
    nums = []
    target = 6
    solu = Solution()
    print(solu.searchRange(nums, target))
