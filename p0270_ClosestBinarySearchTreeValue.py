import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in order with BST
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res, min_diff = -1, sys.maxsize

        def inOrder(node: Optional[TreeNode]):
            nonlocal target, min_diff, res
            if not node:
                return
            diff = node.val - target
            if abs(diff) < min_diff:
                res = node.val
                min_diff = abs(diff)
            if diff == 0:
                return
            elif diff > 0:
                inOrder(node.left)
            elif diff < 0:
                inOrder(node.right)

        inOrder(root)
        return res
