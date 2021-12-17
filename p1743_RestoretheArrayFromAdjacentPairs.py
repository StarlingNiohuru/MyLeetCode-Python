from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nmap = defaultdict(list)
        for p in adjacentPairs:
            nmap[p[0]].append(p[1])
            nmap[p[1]].append(p[0])
        res = []
        for k, v in nmap.items():
            if len(v) == 1:
                res.append(k)
                break
        prev, curr = None, res[0]
        while not prev or len(nmap[curr]) > 1:
            for x in nmap[curr]:
                if x != prev:
                    prev = curr
                    curr = x
                    break
            res.append(curr)
        return res
