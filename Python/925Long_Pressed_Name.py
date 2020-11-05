class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False

        name_index = 0
        typed_index = 0

        last_char = None
        while name_index < len(name) or typed_index < len(typed):
            if name_index < len(name) and typed_index < len(typed) and name[name_index] == typed[typed_index]:
                last_char = name[name_index]
                name_index += 1
                typed_index += 1
            elif typed_index < len(typed) and last_char == typed[typed_index]:
                typed_index += 1
            else:
                return False

        return True

if __name__ == '__main__':
    name = 'alex'
    typed = 'alexxxx'
    solution = Solution()
    print(solution.isLongPressedName(name, typed))
