from typing import List
from queue import PriorityQueue

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        heap = PriorityQueue()
        for a in A:
            heap.put(-a)

        edge1 = -heap.get()
        edge2 = -heap.get()
        edge3 = -heap.get()

        while edge2 + edge3 <= edge1:
            if heap.qsize() != 0:
                edge1 = edge2
                edge2 = edge3
                edge3 = -heap.get()
            else:
                return 0

        return edge1 + edge2 + edge3


if __name__ == '__main__':
    A = [1, 2, 1]
    solution = Solution()
    print(solution.largestPerimeter(A))