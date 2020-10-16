from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        if len(A) == 1:
            return [A[0] * A[0]]
        zero_neighbour = self.binary_search(A)
        pre_pointer = zero_neighbour + 1
        while True:
            if zero_neighbour >= 0 and pre_pointer <= len(A)-1:
                if abs(A[zero_neighbour]) <= abs(A[pre_pointer]):
                    result.append(A[zero_neighbour]*A[zero_neighbour])
                    zero_neighbour -= 1
                else:
                    result.append(A[pre_pointer]*A[pre_pointer])
                    pre_pointer += 1
            elif zero_neighbour >= 0 and pre_pointer > len(A)-1:
                result.append(A[zero_neighbour]*A[zero_neighbour])
                zero_neighbour -= 1
            elif zero_neighbour < 0 and pre_pointer <= len(A)-1:
                result.append(A[pre_pointer]*A[pre_pointer])
                pre_pointer += 1
            else:
                break

        return result

    def binary_search(self, A: List[int]):

        left_border = 0
        right_border = len(A) - 1

        while left_border <= right_border:
            zero_neighbour = left_border + (right_border - left_border) // 2
            if zero_neighbour == left_border or zero_neighbour == right_border:
                return left_border if abs(A[left_border]) <= abs(A[right_border]) else right_border

            if A[zero_neighbour] == 0:
                return zero_neighbour
            elif A[zero_neighbour] < 0:
                left_border = zero_neighbour
            else:
                right_border = zero_neighbour

        return zero_neighbour


if __name__ == '__main__':
    A = [-4,-2,1,3,10]
    # A = [-4,-1,0,3,10]
    solution = Solution()
    print(solution.binary_search(A))
    print(solution.sortedSquares(A))

