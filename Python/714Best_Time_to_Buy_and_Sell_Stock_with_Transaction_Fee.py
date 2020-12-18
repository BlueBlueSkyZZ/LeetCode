from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        profit = [[0, 0] for _ in range(len(prices))]
        profit[0][1] = -prices[0]
        for i in range(1, len(prices)):
            profit[i][0] = max(profit[i-1][0], profit[i-1][1] + prices[i] - fee)
            profit[i][1] = max(profit[i-1][0] - prices[i], profit[i-1][1])
        return profit[len(prices)-1][0]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solution = Solution()
    print(solution.maxProfit(prices, fee))

