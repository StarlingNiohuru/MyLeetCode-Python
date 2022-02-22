from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# DFS. check if all the elements are equal in a sub grid, if so it's a leaf node.
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(subgrid: List[List[int]]):
            node = Node(val=subgrid[0][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            n, first = len(subgrid), subgrid[0][0]
            same_value = True
            for i in range(n):
                for j in range(n):
                    if subgrid[i][j] != first:
                        same_value = False
                        break
                else:
                    continue
                break
            if not same_value:
                node.isLeaf = False
                node.topLeft = dfs([row[:n // 2] for row in subgrid[:n // 2]])
                node.topRight = dfs([row[n // 2:] for row in subgrid[:n // 2]])
                node.bottomLeft = dfs([row[:n // 2] for row in subgrid[n // 2:]])
                node.bottomRight = dfs([row[n // 2:] for row in subgrid[n // 2:]])
            return node

        res = dfs(grid)
        return res
