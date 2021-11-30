from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for n in range(1, len(strs)):
                if i >= len(strs[n]) or strs[0][i] != strs[n][i]:
                    return res
            res += strs[0][i]
        return res
