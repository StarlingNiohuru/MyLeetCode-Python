class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, empty, full = 0, 0, numBottles
        while full > 0:
            res += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        return res
