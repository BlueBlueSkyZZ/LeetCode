from typing import List



class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = Stack()
        for log in logs:
            if log == './':
                pass
            elif log == '../':
                if stack.size() == 0:
                    pass
                else:
                    stack.pop()
            else:
                stack.push(log)
        return stack.size()


class Stack(object):

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]

if __name__ == '__main__':
    solution = Solution()
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
    logs = ["d1/", "../", "../", "../"]
    print(solution.minOperations(logs))