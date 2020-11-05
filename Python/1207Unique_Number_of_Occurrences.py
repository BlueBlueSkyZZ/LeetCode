from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        value_count_arr = [0] * 2001
        for num in arr:
            value_count_arr[num+1000] += 1

        num_count = {}
        for count in value_count_arr:
            if count not in num_count.keys():
                num_count[count] = 1
            else:
                num_count[count] += 1
        for key, value in num_count.items():
            if value > 1 and key != 0:
                return False
        return True


if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    arr = [1, 2]
    solution = Solution()
    print(solution.uniqueOccurrences(arr))