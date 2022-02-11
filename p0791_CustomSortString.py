from collections import defaultdict


# hash map
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        res = ""
        for c in order:
            if count[c] > 0:
                res += c * count[c]
            count[c] = 0
        for c in count:
            if count[c] > 0:
                res += c * count[c]
        return res
