from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0
        arrow_index = 0

        while arrow_index < len(points):
            now_index = arrow_index
            while now_index < len(points) and points[now_index][0] <= points[arrow_index][1]:
                now_index += 1
            arrow_index = now_index
            count += 1

        return count


if __name__ == '__main__':
    points = [[1,2],[2,3]]
    solution = Solution()
    print(solution.findMinArrowShots(points))

