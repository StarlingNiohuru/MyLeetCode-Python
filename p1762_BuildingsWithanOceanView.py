from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        for i in reversed(range(len(heights))):
            if not res or heights[i] > heights[res[-1]]:
                res.append(i)
        res.reverse()
        return res
