from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first = rounds[0]
        last = rounds[-1]
        if first <= last:
            return list(range(first, last + 1))
        else:
            return list(range(1, last + 1)) + list(range(first, n + 1))
