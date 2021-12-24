from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS with level count
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        while q:
            level_len = len(q)
            temp = None
            for i in range(level_len):
                node = q.popleft()
                if node:
                    temp = node.val
                    q.append(node.left)
                    q.append(node.right)
            if temp is not None:  # beware of val==0
                res.append(temp)
        return res
