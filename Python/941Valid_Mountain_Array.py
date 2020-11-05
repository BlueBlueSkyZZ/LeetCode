from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        bottom1 = 0
        top = 0
        bottom2 = 0

        for i in range(len(A)-1):
            if A[i+1] > A[i] and bottom2 == 0:
                top = i+1
            elif A[i+1] < A[i] and top != 0:
                bottom2 = i+1
            else:
                return False

        if top - bottom1 > 0 and bottom2 - top > 0:
            return True

        return False


if __name__ == '__main__':
    A = [3,5,5]
    A = [2,2,3,2,1]
    solution = Solution()
    print(solution.validMountainArray(A))


