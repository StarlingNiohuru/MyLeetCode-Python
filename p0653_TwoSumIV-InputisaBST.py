from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    target = None
    seen = None
    res = None

    def inOrder(self, node: Optional[TreeNode]):
        if self.res:
            return
        if not node:
            return
        self.inOrder(node.left)
        if self.target - node.val in self.seen:
            self.res = True
        else:
            self.seen.add(node.val)
        self.inOrder(node.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.target = k
        self.seen = set()
        self.res = False
        self.inOrder(root)
        return self.res
