from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        x, y = -1, 0
        for i in reversed(range(len(nums))):
            if i > 0 and nums[i] > nums[i - 1]:
                x = i - 1
                break
        if x >= 0:
            for j in reversed(range(len(nums))):
                if nums[j] > nums[x]:
                    y = j
                    break
            nums[x], nums[y] = nums[y], nums[x]
        nums[x + 1:] = sorted(nums[x + 1:])
