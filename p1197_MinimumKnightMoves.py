from collections import deque


# BFS and hash set
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        res = 0
        while len(q) > 0:
            count = len(q)
            for _ in range(count):
                curr = q.popleft()
                if curr[0] == x and curr[1] == y:
                    return res
                for d in directions:
                    ni, nj = curr[0] + d[0], curr[1] + d[1]
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        q.append((ni, nj))
            res += 1
        return -1
