import sys
from typing import List


# Use 2 arrays for max left and min right. Find the leftmost index max left<=min right
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ml, mr, n = 0, sys.maxsize, len(nums)
        max_left, min_right = [], []
        for i in range(n - 1):
            ml = max(ml, nums[i])
            max_left.append(ml)
        for i in range(n - 1, 0, -1):
            mr = min(mr, nums[i])
            min_right.append(mr)
        for i in range(n - 1):
            if max_left[i] <= min_right[n - i - 2]:
                return i + 1
