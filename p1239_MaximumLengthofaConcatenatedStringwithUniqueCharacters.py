from typing import List


# DFS
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n, res = len(arr), 0

        def dfs(i: int, curr: str):
            nonlocal n, res
            if i == n:
                res = max(res, len(curr))
                return
            for j in range(i, n):
                if len(set(curr + arr[j])) == len(curr + arr[j]):
                    dfs(j + 1, curr + arr[j])
                elif j == n - 1:
                    dfs(j + 1, curr)

        dfs(0, "")
        return res
