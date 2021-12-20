from collections import deque, defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS + hash map with row and col. Sort (row,val) in every map[col]
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vmap = defaultdict(list)
        leftmost, rightmost = 0, 0
        q = deque()
        q.append((root, 0, 0))
        while q:
            node, row, col = q.popleft()
            if node:
                vmap[col].append((row, node.val))
                leftmost = min(leftmost, col)
                rightmost = max(rightmost, col)
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))
        res = []
        for i in range(leftmost, rightmost + 1):
            res.append([])
            for row, val in sorted(vmap[i]):
                res[-1].append(val)
        return res
