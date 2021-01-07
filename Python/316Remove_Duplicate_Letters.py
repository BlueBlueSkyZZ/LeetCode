class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        s_map = {}
        s_count = [0]*26
        for i in range(len(s)):
            if s[i] not in s_map.keys():
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1


        result = []
        for i in range(26):
            if s_count[i] != 0:
                result.append(chr(i+ord('a')))

        return "".join(result)


if __name__ == '__main__':
    s = 'bcabc'
    solution = Solution()
    print(solution.removeDuplicateLetters(s))

