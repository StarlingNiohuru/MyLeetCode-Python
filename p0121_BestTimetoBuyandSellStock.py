import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, res = sys.maxsize, 0
        for price in prices:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res
