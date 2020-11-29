from collections import deque


class Solution:
    def sortString(self, s: str) -> str:
        result = []

        char_map = [0] * 26
        for char_s in s:
            char_map[ord(char_s) - ord('a')] += 1

        increase = deque()
        decrease = deque()

        for i in range(len(char_map)):
            if char_map[i] > 0:
                increase.append([chr(i + ord('a')), char_map[i]])

        while len(increase) != 0 or len(decrease) != 0:
            if len(increase) != 0:
                while len(increase) != 0:
                    increase_map = increase.popleft()
                    result.append(increase_map[0])
                    increase_map[1] -= 1
                    if increase_map[1] > 0:
                        decrease.append(increase_map)
            else:
                while len(decrease) != 0:
                    decrease_map = decrease.pop()
                    result.append(decrease_map[0])
                    decrease_map[1] -= 1
                    if decrease_map[1] > 0:
                        increase.appendleft(decrease_map)

        return ''.join(result)

if __name__ == '__main__':
    s = 'rat'
    solution = Solution()
    print(solution.sortString(s))