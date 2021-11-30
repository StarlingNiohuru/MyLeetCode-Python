import sys
from typing import List


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize - 1
        sub_sum = 0
        for i in range(len(nums)):
            sub_sum += nums[i]
            res = max(res, sub_sum)
            sub_sum = max(0, sub_sum)
        return res
