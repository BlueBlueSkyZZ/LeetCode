from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBit(x: int) -> int:
            count = 0
            while x != 0:
                count += x % 2
                x //= 2
            return count

        # arr_bit = [countBit(num) for num in arr]
        return sorted(arr, key=lambda x: (countBit(x), x))


if __name__ == '__main__':
    arr = [0,1,2,3,4,5,6,7,8]
    solution = Solution()
    print(solution.sortByBits(arr))

