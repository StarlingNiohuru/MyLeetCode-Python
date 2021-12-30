import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = None

    def preOrder(self, node: TreeNode, path_max_value):
        if not node:
            return
        if path_max_value <= node.val:
            self.res += 1
            path_max_value = node.val
        self.preOrder(node.left, path_max_value)
        self.preOrder(node.right, path_max_value)

    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.preOrder(root, -sys.maxsize - 1)
        return self.res
