class Solution:
    def _expandFromCentre(self, s: str, l: int, r: int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self._expandFromCentre(s, i, i)
            if len(s1) > len(res):
                res = s1
            s2 = self._expandFromCentre(s, i, i + 1) if i < len(s) - 1 else ""
            if len(s2) > len(res):
                res = s2
        return res
