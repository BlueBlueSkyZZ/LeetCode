from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda point: (point[0]**2 + point[1]**2))
        return points[:K]


if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    K=2
    solution = Solution()
    print(solution.kClosest(points, K))


