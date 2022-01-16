from typing import List


# dfs
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, curr = [], []

        def isValid(ips: str):
            if len(ips) > 1 and ips[0] == "0":
                return False
            return 0 <= int(ips) <= 255

        def dfs(i):
            nonlocal res, curr, s
            if len(curr) == 4:
                if i == len(s):
                    res.append('.'.join(curr))
                return
            for j in [1, 2, 3]:
                if i + j <= len(s) and isValid(s[i:i + j]):
                    curr.append(s[i:i + j])
                    dfs(i + j)
                    curr.pop()

        dfs(0)
        return res
