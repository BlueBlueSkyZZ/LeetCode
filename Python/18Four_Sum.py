from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        nums_len = len(nums)
        if nums_len < 4:
            return []
        nums.sort()
        print(nums)
        for i in range(nums_len-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, nums_len-2):
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                pre_pointer = j + 1
                suf_pointer = nums_len - 1
                while pre_pointer < suf_pointer:
                    four_sum = nums[i] + nums[j] + nums[pre_pointer] + nums[suf_pointer]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[pre_pointer], nums[suf_pointer]])

                        now_pre = nums[pre_pointer]
                        pre_pointer += 1
                        while pre_pointer < nums_len-1 and now_pre == nums[pre_pointer]:
                            pre_pointer += 1

                        now_suf = nums[suf_pointer]
                        suf_pointer -= 1
                        while suf_pointer > 0 and now_suf == nums[suf_pointer]:
                            suf_pointer -= 1
                    elif four_sum < target:
                        now_pre = nums[pre_pointer]
                        pre_pointer += 1
                        while  pre_pointer < nums_len-1 and now_pre == nums[pre_pointer]:
                            pre_pointer += 1
                    else:
                        now_suf = nums[suf_pointer]
                        suf_pointer -= 1
                        while suf_pointer > 0 and now_suf == nums[suf_pointer]:
                            suf_pointer -= 1

        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-2, -1, -1, 1, 1, 2, 2]
    target = 0

    # nums = [0, 0, 0, 0]
    # target = 0

    # nums = [-1,-5,-5,-3,2,5,0,4]
    # target = -7
    solution = Solution()
    print(solution.fourSum(nums, target))

