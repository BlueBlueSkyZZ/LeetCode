class Solution:
    def reorganizeString(self, S: str) -> str:
        char_count = [0] * 26
        max_char_count = 0
        max_char = ''
        for s in S:
            char_count[ord(s) - ord('a')] += 1
            if char_count[ord(s) - ord('a')] > max_char_count:
                max_char_count = char_count[ord(s) - ord('a')]
                max_char = s

        if max_char_count > (len(S) + 1) // 2:
            return ""

        result = [''] * len(S)
        charIndex = 0

        while char_count[ord(max_char) - ord('a')] > 0:
            result[charIndex] = max_char
            char_count[ord(max_char) - ord('a')] -= 1
            charIndex += 2

        for i in range(26):
            while char_count[i] > 0:
                if charIndex >= len(S):
                    charIndex = 1
                result[charIndex] = chr(i + ord('a'))
                charIndex += 2
                char_count[i] -= 1

        return ''.join(result)

if __name__ == '__main__':
    S= 'aab'
    solu = Solution()
    print(solu.reorganizeString(S))








