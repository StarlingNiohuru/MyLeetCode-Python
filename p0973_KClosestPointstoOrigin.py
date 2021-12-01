import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0] * p[0] + p[1] * p[1], p) for p in points]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heap[0][1])
            heapq.heappop(heap)
        return res
