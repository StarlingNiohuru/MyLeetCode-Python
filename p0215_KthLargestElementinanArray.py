import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        res = -heapq.nsmallest(k, heap)[-1]
        return res
