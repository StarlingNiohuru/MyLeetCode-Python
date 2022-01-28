from collections import defaultdict
from typing import List


# hash map with a shift key
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getKey(s: str):
            base = ord(s[0])
            key = ""
            for c in s:
                key += chr((ord(c) - base) % 26 + ord('a'))
            return key

        gmap = defaultdict(list)
        for string in strings:
            hash_key = getKey(string)
            gmap[hash_key].append(string)
        res = list(gmap.values())
        return res
