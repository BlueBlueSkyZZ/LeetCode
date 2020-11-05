from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []
        last_one_char = [0] * 26
        start_index = 0
        end_index = 0

        for i in range(len(S)):
            last_one_char[ord(S[i]) - ord('a')] = i

        for i in range(len(S)):
            end_index = max(end_index, last_one_char[ord(S[i]) - ord('a')])

            if end_index == i:
                result.append(end_index - start_index + 1)
                start_index = end_index + 1

        return result


if __name__ == '__main__':
    S = 'ababcbacadefegdehijhklij'
    solution = Solution()
    print(solution.partitionLabels(S))

