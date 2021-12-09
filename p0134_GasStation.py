from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr, total, res = 0, 0, 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                res = i + 1
            total += gas[i] - cost[i]
        if total < 0:
            res = -1
        return res
