from typing import List


# DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        res = False

        def dfs(i: int, j: int, k: int):
            nonlocal board, word, directions, m, n, visited, res
            if board[i][j] != word[k]:
                return
            elif k == len(word) - 1:
                res = True
                return
            visited[i][j] = True
            for d in directions:
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    dfs(nx, ny, k + 1)
            visited[i][j] = False

        for x in range(m):
            for y in range(n):
                dfs(x, y, 0)
        return res
