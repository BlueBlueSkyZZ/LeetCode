from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        results = [(candy+extraCandies) >= max_candies for candy in candies]
        return results


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    solution = Solution()
    print(solution.kidsWithCandies(candies, extraCandies))

