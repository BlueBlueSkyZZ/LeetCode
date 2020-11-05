from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        return result

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums_set = {}

        for num in nums1:
            if num not in nums_set.keys():
                nums_set[num] = 1

        for num in nums2:
            if num not in nums_set:
                pass
            else:
                nums_set[num] += 1

        for num, val in nums_set.items():
            if val > 1:
                result.append(num)

        return result