from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        nums_count = {}
        tail = {}

        for num in nums:
            if num not in nums_count.keys():
                nums_count[num] = 1
                tail[num] = 0
            else:
                nums_count[num] += 1

        for num in nums:
            if nums_count[num] == 0:
                continue
            elif nums_count[num] > 0 and num-1 in tail.keys() and tail[num-1] > 0:
                nums_count[num] -= 1
                tail[num-1] -= 1
                tail[num] += 1
            elif nums_count[num] > 0 and \
                    num+1 in tail.keys() and nums_count[num+1] > 0 and \
                    num+2 in tail.keys() and nums_count[num+2] > 0:
                nums_count[num] -= 1
                nums_count[num+1] -= 1
                nums_count[num+2] -= 1
                tail[num+2] += 1
            else:
                return False

        return True


if __name__ == '__main__':
    nums = [1,2,3,3,4,4,5,6]
    solution = Solution()
    print(solution.isPossible(nums))

