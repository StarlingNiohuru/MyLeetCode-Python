from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        for i in range(n + 1):
            for j in range(i):
                if len(dp[j]) > 0 and s[j:i] in wordDict:
                    for x in dp[j]:
                        temp = x + " " + s[j:i] if len(x) else s[j:i]
                        dp[i].append(temp)
        return dp[n]
