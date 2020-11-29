from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        now_place = 0
        max_palce = 1
        max_num = nums[0]

        while now_place < max_palce:
            buckets = [[] for _ in range(10)]
            for num in nums:
                if now_place == 0:
                    max_num = max(max_num, num)
                    max_palce = len(str(max_num))
                buckets[(num//(10**now_place)) % 10].append(num)
            temp_nums = []
            for bucket in buckets:
                for one_num in bucket:
                    temp_nums.append(one_num)
            nums = temp_nums
            now_place += 1

        return max(nums[i] - nums[i-1] for i in range(1, len(nums)))


