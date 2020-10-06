from typing import List
import datetime

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        result = []

        name_map = {}
        for i in range(len(keyName)):
            if keyName[i] not in name_map.keys():
                name_map[keyName[i]] = []
            time_date = datetime.datetime.strptime(keyTime[i], "%H:%M")
            name_map[keyName[i]].append(time_date)

        for name, times in name_map.items():
            if len(times) < 3:
                continue
            times = sorted(times, reverse=False)
            for i in range(len(times)-2):
                delta_time = times[i+2] - times[i]
                threshold = datetime.timedelta(hours=1)
                if delta_time <= threshold and delta_time.days == 0:
                    result.append(name)
                    break
        new_result = sorted(result, reverse=False)
        return new_result


if __name__ == '__main__':
    keyName = ["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"]
    keyTime = ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]

    keyName=["j", "j", "j"]
    keyTime=["23:58", "23:59", "00:01"]

    keyName = ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"]
    keyTime = ["04:48", "23:53", "06:36", "07:45", "12:16", "00:52", "10:59", "17:16", "00:36", "01:26", "22:42"]
    solution = Solution()
    print(solution.alertNames(keyName, keyTime))