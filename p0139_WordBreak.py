from typing import List


# dp[i] covers s[0,i-1]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
