from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increasing, decreasing = False, False
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                increasing = True
            elif nums[i] > nums[i + 1]:
                decreasing = True
            if increasing and decreasing:
                return False
        return True
