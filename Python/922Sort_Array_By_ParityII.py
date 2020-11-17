from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1

        def swap(A: List[int], x, y):
            temp = A[x]
            A[x] = A[y]
            A[y] = temp

        for i in range(len(A)//2):
            if A[2*i] % 2 == 0:
                pass
            else:
                while A[odd] % 2 != 0:
                    odd += 2
                swap(A, odd, 2*i)

        return A

