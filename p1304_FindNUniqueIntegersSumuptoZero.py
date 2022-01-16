from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0 for _ in range(n)]
        total = 0
        for i in range(1, n):
            res[i] = i
            total += i
        res[0] = -total
        return res
