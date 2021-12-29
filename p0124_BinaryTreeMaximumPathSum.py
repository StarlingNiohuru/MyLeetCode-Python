import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# post order traverse, every loop returns path from root to some node. find left path(>=0)+ right path(>=0)+ node.val
class Solution:
    res = None

    def maxPathFromRoot(self, node: TreeNode):
        if not node:
            return 0
        left = max(0, self.maxPathFromRoot(node.left))
        right = max(0, self.maxPathFromRoot(node.right))
        self.res = max(self.res, node.val + left + right)
        return node.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -sys.maxsize - 1
        self.maxPathFromRoot(root)
        return self.res
