from collections import defaultdict


# hash map with list( map[index]=list[(snap_id,value)...]) and upper bound of binary search
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.vmap = defaultdict(list)
        for i in range(length):
            self.vmap[i].append((0, 0))

    def set(self, index: int, val: int) -> None:
        if self.vmap[index][-1][0] == self.snap_id:
            self.vmap[index].pop()
        self.vmap[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        vlist = self.vmap[index]
        lo, hi = 0, len(vlist)
        while lo < hi:
            mid = (lo + hi) // 2
            if vlist[mid][0] <= snap_id:
                lo = mid + 1
            else:
                hi = mid
        return vlist[lo - 1][1]
