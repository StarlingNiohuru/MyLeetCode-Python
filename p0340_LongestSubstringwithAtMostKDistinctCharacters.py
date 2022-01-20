from collections import defaultdict


# hash map and sliding window
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i, j, res = 0, 0, 0
        for j in range(len(s)):
            count[s[j]] += 1
            while len(count) > k:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    count.pop(s[i])
                i += 1
            res = max(res, j - i + 1)
        return res
