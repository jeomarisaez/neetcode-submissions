class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        for d in t:
            if d not in t_map:
                t_map[d] = 1
            else:
                t_map[d] += 1
        if s_map == t_map:
            return True
        else:
            return False

            