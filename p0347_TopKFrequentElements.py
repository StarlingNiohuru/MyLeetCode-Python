import heapq
from collections import defaultdict
from typing import List


# hash map and heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heap[0][1])
            heapq.heappop(heap)
        return res
