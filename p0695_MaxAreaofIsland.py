from typing import List


class Solution:
    grid = None
    m = None
    n = None
    count = None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(self, i: int, j: int):
        if self.grid[i][j] == 0:
            return
        else:
            self.grid[i][j] = 0
            self.count += 1
        for d in self.directions:
            nx = i + d[0]
            ny = j + d[1]
            if 0 <= nx < self.m and 0 <= ny < self.n:
                self.dfs(nx, ny)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.count = 0
                    self.dfs(i, j)
                    res = max(res, self.count)
        return res
