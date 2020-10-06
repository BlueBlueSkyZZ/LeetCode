from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memery = []
        result = []
        for i in range(len(nums)):
            if nums[i] in memery:
                result.append(memery.index(nums[i]))
                result.append(i)
                break
            memery.append(target - nums[i])
        return result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    nums = [3, 2, 4]
    target = 6

    solution = Solution()
    print(solution.twoSum(nums, target))

