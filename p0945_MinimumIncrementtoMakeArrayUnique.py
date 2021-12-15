from typing import List


# sort and arrange the list by greedy way
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                temp = nums[i - 1] - nums[i] + 1
                res += temp
                nums[i] += temp
        return res
