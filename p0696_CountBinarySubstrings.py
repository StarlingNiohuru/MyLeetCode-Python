# Keep a list of length of consecutive same-digit sub string.For every 2 adjacent sub strings, min() is the total they
# provide. answer is the sum of every pair.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        sub_counts = [1]
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                sub_counts[-1] += 1
            else:
                sub_counts.append(1)
        res = 0
        for i in range(1, len(sub_counts)):
            res += min(sub_counts[i - 1], sub_counts[i])
        return res
