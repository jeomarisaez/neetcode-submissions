class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        chars = "abcdefghijklmnopqrstuvwxyz"
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tupled_count = tuple(count)
            if tupled_count in hash_map:
                hash_map[tupled_count].append(s)
            else:
                hash_map[tupled_count] = [s]
        return list(hash_map.values())