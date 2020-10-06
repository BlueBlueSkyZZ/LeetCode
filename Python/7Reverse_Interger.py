class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        signal = True if x >= 0 else False
        x = x if x >= 0 else -x
        remainers = []
        while x != 0:
            remainer = x % 10
            x = x // 10
            remainers.append(remainer)

        result = 0
        for i in range(len(remainers)):
            result += remainers[i] * (10 ** (len(remainers) - i - 1))
            if result > 2**32 - 1:
                return 0
        result = result if signal else -result
        return result

    def reverse2(self, x: int) -> int:
        rev = 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)
        while x != 0:
            remainer = x % 10 if x > 0 else x % (-10)
            x = x // 10 if x > 0 else int(x / 10)
            if rev > INT_MAX / 10 or (rev == INT_MAX / 10 and remainer > 7):
                return 0
            if rev < INT_MIN / 10 or (rev == INT_MIN / 10 and remainer < -8):
                return 0
            rev = rev * 10 + remainer
        return rev


if __name__ == '__main__':
    print(-123%10)
    solution = Solution()
    print(solution.reverse2(-123))

