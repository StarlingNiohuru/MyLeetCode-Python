# dp[i][j] means if s[i:] match p[j:]. Scan the dp table [m+1,n+1] from (m,n-1) to (0,0)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (s[i] == p[j] or p[j] == ".")
                if j < n - 1 and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]
