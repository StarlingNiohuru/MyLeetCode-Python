from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        res = 0
        for t in time:
            temp = t % 60
            res += count.get((60 - temp) % 60, 0)
            count[temp] = count.get(temp, 0) + 1
        return res
