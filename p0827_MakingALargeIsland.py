from typing import List


# DFS to label each island with a label and count each area. For every 0, checks its 4 neighbours to get the merged
# area. Find the max.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)
        label_grid = [[0] * n for _ in range(n)]
        area_map = {}

        def dfs(x: int, y: int):
            nonlocal directions, n, label_grid, label, area
            label_grid[x][y] = label
            area += 1
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 0 and label_grid[nx][ny] == 0:
                    dfs(nx, ny)

        label = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0 and label_grid[i][j] == 0:
                    area = 0
                    dfs(i, j)
                    area_map[label] = area
                    label += 1
        res = max(area_map.values()) if len(area_map) else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbours = set()
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < n and label_grid[ni][nj] > 0:
                            neighbours.add(label_grid[ni][nj])
                    merged_area = 1
                    for k in neighbours:
                        merged_area += area_map[k]
                    res = max(res, merged_area)
        return res
