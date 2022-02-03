from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        direct = 0
        for diag in range(m + n - 1):
            if direct % 2 == 0:
                i, j = min(diag, m - 1), diag - min(diag, m - 1)
            else:
                i, j = diag - min(diag, n - 1), min(diag, n - 1)
            while 0 <= i < m and 0 <= j < n:
                res.append(mat[i][j])
                if direct % 2 == 0:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            direct += 1
        return res
