import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for node in lists:
            if node:
                heap.append((node.val, counter, node))
            counter += 1
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            p = heap[0]
            heapq.heappop(heap)
            curr.next = p[2]
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, counter, curr.next))
                counter += 1
        return dummy.next
