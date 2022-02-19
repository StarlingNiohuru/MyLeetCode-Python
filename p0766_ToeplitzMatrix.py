from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for d in range(m - 1, -n, -1):
            i, j = max(d, 0), max(d, 0) - d
            first = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != first:
                    return False
                i += 1
                j += 1
        return True
