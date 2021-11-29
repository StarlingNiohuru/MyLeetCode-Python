from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    seen = set()
    target = None
    res = False

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
        self.inOrder(root)
        self.seen.clear()
        return self.res
