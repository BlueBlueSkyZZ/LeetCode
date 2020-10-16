from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result_map = {}
        for word in A:
            word_map = {}
            for character in word:
                if character in word_map.keys():
                    word_map[character] += 1
                else:
                    word_map[character] = 1
            if result_map == {}:
                result_map = word_map
            else:
                for key, val in result_map.items():
                    if key not in word_map.keys():
                        result_map[key] = 0
                    else:
                        result_map[key] = min(result_map[key], word_map[key])
        result = []
        for key, val in result_map.items():
            for i in range(val):
                result.append(key)
        print(result)

if __name__ == '__main__':
    A = ["bella", "label", "roller"]
    # A = ["cool","lock","cook"]
    solution = Solution()
    solution.commonChars(A)
