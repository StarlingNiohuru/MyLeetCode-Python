from typing import List


# Find the max and sum in each group of same char. Add sum-max to res
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res, i = 0, 0
        while i < len(colors):
            max_cost, sum_cost = 0, 0
            char = colors[i]
            while i < len(colors) and colors[i] == char:
                sum_cost += neededTime[i]
                max_cost = max(max_cost, neededTime[i])
                i += 1
            res += sum_cost - max_cost
        return res
