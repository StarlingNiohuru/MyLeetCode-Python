from typing import List


# sort by cost[0]-cost[1]
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) / 2
        res = 0
        for i, cost in enumerate(costs):
            if i < n:
                res += cost[0]
            else:
                res += cost[1]
        return res
