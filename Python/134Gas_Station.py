from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        left = 0
        gas_sum = 0
        cost_sum = 0

        for i in range(len(gas)):
            gas_sum += gas[i]
            cost_sum += cost[i]
            left += gas[i] - cost[i]
            if left < 0:
                start = i+1
                left = 0

        if cost_sum > gas_sum:
            return -1

        return start


