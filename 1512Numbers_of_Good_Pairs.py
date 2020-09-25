from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        用字典统计
        :param nums:
        :return:
        """
        result_dict = {}
        result_count = 0
        for num in nums:
            if num not in result_dict.keys():
                result_dict[num] = 1
            else:
                result_count += result_dict[num]
                result_dict[num] += 1
        return result_count


    def numIdenticalPairs2(self, nums: List[int]) -> int:
        """
        开辟额外的数组空间进行统计，注意num的条件是小于100所以开辟了数组长度为100
        :param nums:
        :return:
        """
        result_count = 0
        temp = [0] * 100
        for num in nums:
            result_count += temp[num-1]
            temp[num-1] += 1
        return result_count


if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 2, 3, 1, 1, 3]
    # nums = [1, 1, 1, 1]
    # nums = [1, 2, 3]
    nums = [5,5,1,77,96,96,89,80,12,23,1,6,3,66,39,88,48,38,44,32,44,36,60,87,53,77,72,49,13,39,60,60,71,68,80,75,79,38,4,14,59,75,6,91,87,95,25,55,83,18,26,59,53,100,42,96,76,22,21,4,22,46,34,39,98,82,54,73,52,33,47,73,54,23,82,98,13,51,52,1,96,69,76]
    # print(solution.numIdenticalPairs(nums))
    print(solution.numIdenticalPairs2(nums))