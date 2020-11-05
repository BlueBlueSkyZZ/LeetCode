from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_val = newInterval[0]
        end_val = newInterval[1]
        result = []

        append_flag = False

        for interval in intervals:
            if interval[1] < start_val:
                result.append(interval)
            elif interval[0] > end_val:
                if not append_flag:
                    result.append([start_val, end_val])
                    append_flag = True
                result.append(interval)
            else:
                start_val = min(interval[0], start_val)
                end_val = max(interval[1], end_val)
        if not append_flag:
            result.append([start_val, end_val])

        return result


if __name__ == '__main__':
    intervals = []
    newInterval = [5, 7]
    solution = Solution()
    print(solution.insert(intervals, newInterval))

