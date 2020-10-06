from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 - runningCost <= 0:
            return -1

        queuelist = 0
        max_profit = -1
        profit = 0
        cycle = 0
        max_cycle = -1

        for customer in customers:
            cycle += 1
            if queuelist + customer <= 4:
                profit += (queuelist + customer) * boardingCost - runningCost
                queuelist = 0
            else:
                profit += 4 * boardingCost - runningCost
                queuelist += customer - 4

            if profit > max_profit:
                max_profit = profit
                max_cycle = cycle

        while queuelist > 0:
            cycle += 1
            if queuelist <= 4:
                profit += queuelist * boardingCost - runningCost
                queuelist = 0
            else:
                profit += 4 * boardingCost - runningCost
                queuelist -= 4

            if profit > max_profit:
                max_profit = profit
                max_cycle = cycle

        return max_cycle


if __name__ == '__main__':
    solution = Solution()

    customers = [8, 3]
    boardingCost = 5
    runningCost = 6

    # customers = [10,9,6]
    # boardingCost = 6
    # runningCost = 4

    # customers = [3,4,0,5,1]
    # boardingCost = 1
    # runningCost = 92

    # customers = [10, 10, 6, 4, 7]
    # boardingCost = 3
    # runningCost = 8
    print(solution.minOperationsMaxProfit(customers, boardingCost, runningCost))