from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_map:
                return [index_map[complement], i]
            else:
                index_map[nums[i]] = i
