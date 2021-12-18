from collections import defaultdict
from typing import List


# hash map with list and sort
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dmap = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                dmap[i - j].append(mat[i][j])
        for v in dmap.values():
            v.sort()
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mat[i][j] = dmap[i - j].pop()
        return mat
