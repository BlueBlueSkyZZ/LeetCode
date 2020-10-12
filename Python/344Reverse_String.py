from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            swap(s, i, len(s)-1-i)
        # print(s)

def swap(s, list_i, list_j):
    temp = s[list_i]
    s[list_i] = s[list_j]
    s[list_j] = temp


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    s = ["H","a","n","n","a","h"]
    solution = Solution()
    solution.reverseString(s)

