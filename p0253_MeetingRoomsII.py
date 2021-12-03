import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heapify(heap)
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        res = len(heap)
        return res
