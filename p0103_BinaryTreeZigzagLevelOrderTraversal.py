from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS of level and count
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level, count = 0, 0
        q = deque([root])
        while len(q):
            count = len(q)
            row = []
            for i in range(count):
                node = q.popleft()
                if node:
                    row.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level % 2:
                row.reverse()
            level += 1
            if len(row):
                res.append(row.copy())
        return res
