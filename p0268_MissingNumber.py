from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] >= n or nums[i] == i or nums[i] == nums[nums[i]]:
                i += 1
            else:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
        i = 0
        while i < n and i == nums[i]:
            i += 1
        return i
