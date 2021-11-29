from typing import List


# hash map of pre_sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        sum_map = {0: 1}
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            res += sum_map.get(pre_sum - k, 0)
            sum_map[pre_sum] = sum_map.get(pre_sum, 0) + 1
        return res
