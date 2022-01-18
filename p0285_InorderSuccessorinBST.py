from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BST
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        curr, res = root, None
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                res = curr
                curr = curr.left
        return res
