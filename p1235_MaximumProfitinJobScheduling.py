from typing import List


# dp[i] is the max profit in [0,1]. dp[i]=max(dp[i-1],dp[j]+profit[i]) where the end time of j is just before the
# start time of i.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        n = len(startTime)
        dp = [0 for _ in range(n)]
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        for i in range(n):
            max_profit = 0
            for j in range(i - 1, -1, -1):
                if jobs[j][1] <= jobs[i][0]:
                    max_profit = dp[j]
                    break
            prev_profit = dp[i - 1] if i > 0 else 0
            dp[i] = max(max_profit + jobs[i][2], prev_profit)
        return dp[n - 1]
