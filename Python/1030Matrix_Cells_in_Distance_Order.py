from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        distance = []

        for i in range(R):
            for j in range(C):
                distance.append([i, j])

        distance.sort(key=lambda x: (abs(x[0] - r0) + abs(x[1] - c0)))
        return distance


if __name__ == '__main__':
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    solution = Solution()
    print(solution.allCellsDistOrder(R, C, r0, c0))