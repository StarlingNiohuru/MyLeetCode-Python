class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        imap = {}
        i, j, res = 0, 0, 0
        while i < len(s):
            if s[i] in imap:
                if imap[s[i]] >= j:
                    j = imap[s[i]] + 1
            imap[s[i]] = i
            res = max(res, i - j + 1)
            i += 1
        return res
