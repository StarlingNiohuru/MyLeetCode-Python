from typing import List


# DFS
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        start = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        border = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int):
            nonlocal visited, border
            visited[x][y] = True
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == start and not visited[nx][ny]:
                    dfs(nx, ny)
                elif nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != start:
                    border[x][y] = True

        dfs(row, col)
        res = []
        for i in range(m):
            res.append([])
            for j in range(n):
                if border[i][j]:
                    res[-1].append(color)
                else:
                    res[-1].append(grid[i][j])
        return res
