from typing import List


# If a%c==b%c, (a-b)%c==0. pre sum and hash map of {mod of curr pre sum:first index}.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mmap = {0: -1}
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            curr_mod = pre_sum % k
            if curr_mod in mmap:
                if mmap[curr_mod] + 1 < i:
                    return True
            else:
                mmap[curr_mod] = i
        return False
