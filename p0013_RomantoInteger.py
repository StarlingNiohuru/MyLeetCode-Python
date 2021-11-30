class Solution:
    def romanToInt(self, s: str) -> int:
        cmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i == len(s) - 1 or cmap[s[i]] >= cmap[s[i + 1]]:
                sign = 1
            else:
                sign = -1
            res += (sign * cmap[s[i]])
        return res
