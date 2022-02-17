import heapq
from collections import defaultdict
from typing import List


# greedy,hash map and heap
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = defaultdict(int)
        for a in arr:
            count[a] += 1
        heap = [(v, k) for k, v in count.items()]
        heapq.heapify(heap)
        while k > 0:
            curr = heapq.heappop(heap)
            k -= curr[0]
        res = len(heap)
        if k < 0:
            res += 1
        return res
