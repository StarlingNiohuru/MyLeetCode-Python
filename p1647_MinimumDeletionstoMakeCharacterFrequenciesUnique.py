import sys
from collections import defaultdict


# Sort by freq of char and minus each value by greedy way
class Solution:
    def minDeletions(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        res, prev = 0, sys.maxsize
        for freq in sorted(count.values(), reverse=True):
            if freq >= prev:
                res += freq - prev + 1 if prev > 0 else freq
                prev -= 1 if prev > 0 else 0
            else:
                prev = freq
        return res
