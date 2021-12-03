from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] <= 0 or nums[i] > n or nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        i = 0
        while i < n and nums[i] == i + 1:
            i += 1
        return i + 1
