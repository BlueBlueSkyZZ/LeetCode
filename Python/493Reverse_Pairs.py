from typing import List


class Solution:

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        result = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)

        i = left
        j = mid + 1

        while i <= mid:
            while j <= right and (nums[i] > 2 * nums[j]):
                j += 1
            result += j - (mid + 1)
            i += 1

        temp_nums = [0] * (right-left+1)
        pl = left
        pr = mid + 1
        pt = 0
        while pl <= mid or pr <= right:
            if pl > mid:
                temp_nums[pt:] = nums[pr:right + 1]
                break
            elif pr > right:
                temp_nums[pt:] = nums[pl:mid + 1]
                break
            else:
                if nums[pl] <= nums[pr]:
                    temp_nums[pt] = nums[pl]
                    pl += 1
                    pt += 1
                else:
                    temp_nums[pt] = nums[pr]
                    pr += 1
                    pt += 1
        nums[left:right+1] = temp_nums

        return result

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        return self.merge_sort(nums, 0, len(nums)-1)


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 1]
    solution = Solution()
    print(solution.reversePairs(nums))
