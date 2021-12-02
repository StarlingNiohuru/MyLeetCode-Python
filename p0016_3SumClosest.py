import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sys.maxsize
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return target
                elif sum3 < target:
                    j += 1
                else:
                    k -= 1
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
        return res
