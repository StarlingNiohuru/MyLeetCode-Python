from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        rooms, res = truckSize, 0
        for box_type in boxTypes:
            if rooms >= box_type[0]:
                res += (box_type[0] * box_type[1])
                rooms -= box_type[0]
            else:
                res += (rooms * box_type[1])
                break
        return res
