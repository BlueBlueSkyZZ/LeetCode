from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(len(result[i])):
                if j != 0 and j != i:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result


if __name__ == '__main__':
    solution = Solution()
    numRows = 5
    print(solution.generate(numRows))