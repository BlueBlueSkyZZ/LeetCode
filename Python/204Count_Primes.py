class Solution:
    def countPrimes(self, n: int) -> int:
        primes_mark = [1] * n
        primes = []
        for i in range(2, n):
            if primes_mark[i] == 1:
                primes.append(i)

            for prime in primes:
                if prime * i < n:
                    primes_mark[i * prime] = 0
                else:
                    break

                if i % prime == 0:
                    break

        return len(primes)


if __name__ == '__main__':
    n = 499979
    solution = Solution()
    print(solution.countPrimes(n))
