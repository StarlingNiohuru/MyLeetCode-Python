from collections import deque
from typing import List


# BFS and sort
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([tuple(start)])
        visited = set()
        visited.add(tuple(start))
        distance = 0
        candidate = []
        while len(q) > 0:
            count = len(q)
            for i in range(count):
                x, y = q.popleft()
                if low <= grid[x][y] <= high:
                    candidate.append((distance, grid[x][y], x, y))
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0 and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            distance += 1
        candidate.sort()
        res = []
        for i in range(min(k, len(candidate))):
            _, _, x, y = candidate[i]
            res.append([x, y])
        return res
