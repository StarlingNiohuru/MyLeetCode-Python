from typing import List


# hash set two sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen.clear()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], complement, nums[j]])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return res
