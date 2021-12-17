from typing import List


# 2 pointers
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [[""] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = box[m - j - 1][i]
        for j in range(m):
            k = n - 1
            for i in range(n - 1, -1, -1):
                if res[i][j] == "#":
                    res[i][j], res[k][j] = res[k][j], res[i][j]
                    k -= 1
                elif res[i][j] == "*":
                    k = i - 1
        return res
