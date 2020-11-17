from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {}
        for i in range(len(arr2)):
            arr2_map[arr2[i]] = i
        arr1.sort(key=lambda x: arr2_map[x] if x in arr2_map.keys() else x+len(arr2))
        return arr1


if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    solition = Solution()
    solition.relativeSortArray(arr1, arr2)

