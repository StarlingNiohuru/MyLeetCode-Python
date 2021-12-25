from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS. Subtree may have the answer
class Solution:
    res = None

    def maxDepth(self, node: Optional[TreeNode]):
        if not node:
            return 0
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        self.res = max(self.res, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.maxDepth(root)
        return self.res
