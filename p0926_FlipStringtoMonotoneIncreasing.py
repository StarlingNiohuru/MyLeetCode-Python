import sys


# The final result is like '0'*i+'1'*j. For each i in len(s), flip all the 1 before s[i] and 0 after s[i]. Find the min.
# Use pre sum to get it.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        pre_sum = [0]
        for c in s:
            pre_sum.append(pre_sum[-1] + int(c))
        res = sys.maxsize
        for i in range(len(s) + 1):
            res = min(res, pre_sum[i] + len(s) - i - (pre_sum[-1] - pre_sum[i]))
        return res
