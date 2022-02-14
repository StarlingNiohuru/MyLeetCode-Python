from collections import defaultdict
from typing import List


# convert it to a problem of subarray sum ==k and use hash map of pre sum
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1
        res = 0
        for num in nums:
            n = num % 2
            pre_sum += n
            res += sum_map[pre_sum - k]
            sum_map[pre_sum] += 1
        return res
