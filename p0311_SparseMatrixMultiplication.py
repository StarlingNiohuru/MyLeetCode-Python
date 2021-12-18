from typing import List


# For every mat1[i][x]!=0, calculate its contribute to new[i][j].
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k = len(mat1), len(mat2[0]), len(mat1[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for x in range(k):
                if mat1[i][x]:
                    for j in range(n):
                        if mat2[x][j]:
                            res[i][j] += mat1[i][x] * mat2[x][j]
        return res
