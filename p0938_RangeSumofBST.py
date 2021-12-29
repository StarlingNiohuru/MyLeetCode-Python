from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in order traverse
class Solution:
    low = None
    high = None
    res = None

    def inOrder(self, node: TreeNode):
        if not node:
            return
        self.inOrder(node.left)
        if self.low <= node.val <= self.high:
            self.res += node.val
        self.inOrder(node.right)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.res = 0
        self.inOrder(root)
        return self.res
