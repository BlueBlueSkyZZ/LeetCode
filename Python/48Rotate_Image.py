from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_len = len(matrix)

        for i in range(edge_len // 2):
            for j in range(edge_len):
                matrix[i][j], matrix[edge_len - i - 1][j] = matrix[edge_len - i - 1][j], matrix[i][j]

        for i in range(edge_len):
            for j in range(i+1, edge_len):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
