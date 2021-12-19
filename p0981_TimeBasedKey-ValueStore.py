from collections import defaultdict


# dict with list and upper bound of binary search
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        tlist = self.tmap[key]
        lo, hi = 0, len(tlist)
        while lo < hi:
            mid = (lo + hi) // 2
            if tlist[mid][0] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        return tlist[lo - 1][1] if lo > 0 else ""
