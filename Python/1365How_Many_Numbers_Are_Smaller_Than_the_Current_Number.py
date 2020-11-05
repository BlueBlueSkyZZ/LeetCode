from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_arr = [0] * 101
        result = []
        for num in nums:
            count_arr[num] += 1

        for i in range(1, 101):
            count_arr[i] += count_arr[i-1]

        for num in nums:
            result.append(count_arr[num-1] if num > 0 else 0)

        return result


if __name__ == '__main__':
    nums = [8,1,2,2,3]
    nums = [7,7,7,7]
    nums = [5,0,10,0,10,6]
    solution = Solution()
    print(solution.smallerNumbersThanCurrent(nums))

