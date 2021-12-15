from collections import deque, defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS and hashmap
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vmap = defaultdict(list)
        q = deque()
        q.append((root, 0))
        leftmost, rightmost = 0, 0
        while q:
            node, i = q.popleft()
            if node:
                vmap[i].append(node.val)
                q.append((node.left, i - 1))
                leftmost = min(leftmost, i)
                q.append((node.right, i + 1))
                rightmost = max(rightmost, i)
        res = [vmap[j] for j in range(leftmost, rightmost + 1)]
        return res
