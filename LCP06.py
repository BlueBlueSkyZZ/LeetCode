from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        """
        除2后保证向上取整就行
        :param coins:
        :return:
        """
        count = 0
        for coins_one_cluster in coins:
            count += (coins_one_cluster + 1) // 2
        return count

    def minCount2(self, coins: List[int]) -> int:
        return sum((coins_one_cluster + 1) // 2 for coins_one_cluster in coins)


if __name__ == '__main__':
    coins = [2, 3, 10]
    solution = Solution()
    print(solution.minCount(coins))
    print(solution.minCount2(coins))
