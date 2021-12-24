import random
from typing import List


# pre sum and binary search of upper bounder
class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = [0]
        for wi in w:
            temp = self.pre_sum[-1]
            self.pre_sum.append(temp + wi)

    def pickIndex(self) -> int:
        target = self.pre_sum[-1] * random.random()
        lo, hi = 0, len(self.pre_sum)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.pre_sum[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
