from collections import defaultdict
from typing import List


# brute force with sparse adjacent matrix
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(list)
        for road in roads:
            edges[road[0]].append(road[1])
            edges[road[1]].append(road[0])
        res = 0
        for i in range(n):
            for j in range(i):
                rank = len(edges[i]) + len(edges[j])
                if i in edges[j]:
                    rank -= 1
                res = max(res, rank)
        return res
