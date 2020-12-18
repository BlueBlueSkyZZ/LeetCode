class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_array = [0] * 26
        t_array = [0] * 26
        for i in range(len(t)):
            t_array[ord(t[i]) - ord('a')] += 1
            if i != len(t) - 1:
                s_array[ord(s[i]) - ord('a')] += 1
        for i in range(26):
            if s_array[i] != t_array[i]:
                return chr(i+ord('a'))


if __name__ == '__main__':
    s = "eae"
    t = "eaae"
    solution = Solution()
    print(solution.findTheDifference(s, t))