class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        if n > 1:
            dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
