from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count_sum = {}
        for a in A:
            for b in B:
                if a+b not in count_sum.keys():
                    count_sum[a+b] = 1
                else:
                    count_sum[a+b] += 1

        result = 0
        for c in C:
            for d in D:
                if -c-d not in count_sum.keys():
                    pass
                else:
                    result += count_sum[-c-d]

        return result