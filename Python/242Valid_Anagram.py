class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for s_char in s:
            if s_char not in s_map.keys():
                s_map[s_char] = 1
            else:
                s_map[s_char] += 1

        for t_char in t:
            if t_char not in t_map.keys():
                t_map[t_char] = 1
            else:
                t_map[t_char] += 1

        if len(s_map.keys()) != len(t_map.keys()):
            return False

        for key, num in s_map.items():
            if key not in t_map.keys():
                return False
            if t_map[key] != num:
                return False

        return True