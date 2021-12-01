from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n, x, y, d = len(matrix), len(matrix[0]), 0, 0, 0
        res = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m * n):
            res.append(matrix[x][y])
            visited[x][y] = True
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            if not (0 <= nx < m and 0 <= ny < n and not visited[nx][ny]):
                d = (d + 1) % 4
                nx = x + directions[d][0]
                ny = y + directions[d][1]
            x, y = nx, ny
        return res
