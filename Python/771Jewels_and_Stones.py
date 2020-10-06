class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for one_char in S:
            if one_char in J:
                count += 1
        return count

def test1():
    solution = Solution()
    J = 'aA'
    S = 'aAAbbb'
    print(solution.numJewelsInStones(J, S))


def test2():
    solution = Solution()
    J = 'z'
    S = 'ZZ'
    print(solution.numJewelsInStones(J, S))

if __name__ == '__main__':
    test1()
    test2()

