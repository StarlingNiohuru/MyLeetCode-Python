from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        for s in strs:
            key = tuple(sorted(s))
            freq_map[key] = freq_map.get(key, []) + [s]
        return freq_map.values()
