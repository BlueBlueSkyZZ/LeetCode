from queue import Queue
from collections import deque

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = deque()
        for i in range(len(S)):
            if S[i] != '#':
                s_stack.append(S[i])
            else:
                if len(s_stack) > 0:
                    s_stack.pop()

        t_stack = deque()
        for i in range(len(T)):
            if T[i] != '#':
                t_stack.append(T[i])
            else:
                if len(t_stack) > 0:
                    t_stack.pop()

        if len(s_stack) != len(t_stack):
            return False

        while len(t_stack) > 0:
            t_str = t_stack.pop()
            s_str = s_stack.pop()
            if t_str != s_str:
                return False

        return True

    def backspaceCompare2(self, S: str, T: str) -> bool:
        skip_s = 0
        skip_t = 0

        s_pointer = len(S) - 1
        t_pointer = len(T) - 1

        while s_pointer >= 0 or t_pointer >= 0:
            while s_pointer >= 0:
                if S[s_pointer] == '#':
                    s_pointer -= 1
                    skip_s += 1
                elif skip_s > 0:
                    skip_s -= 1
                    s_pointer -= 1
                else:
                    break

            while t_pointer >= 0:
                if T[t_pointer] == '#':
                    t_pointer -= 1
                    skip_t += 1
                elif skip_t > 0:
                    skip_t -= 1
                    t_pointer -= 1
                else:
                    break

            if s_pointer >= 0 and t_pointer >= 0:
                if S[s_pointer] != T[t_pointer]:
                    return False
                else:
                    s_pointer -= 1
                    t_pointer -= 1
            else:
                if s_pointer >= 0 or t_pointer >= 0:
                    return False

        return True

if __name__ == '__main__':
    S='ab#c'
    T='ab#c#c'
    S='ab##'
    T='c#d#'
    S='a#c'
    T='b'
    solution = Solution()
    # print(solution.backspaceCompare(S,T))
    print(solution.backspaceCompare2(S,T))