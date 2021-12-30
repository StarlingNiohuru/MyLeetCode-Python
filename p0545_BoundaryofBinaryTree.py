from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    res = []

    def leftBoundaryWithoutLeave(self, node: TreeNode):
        if not node or (not node.left and not node.right):
            return
        self.res.append(node.val)
        if node.left:
            self.leftBoundaryWithoutLeave(node.left)
        else:
            self.leftBoundaryWithoutLeave(node.right)

    def rightBoundaryWithoutLeave(self, node: TreeNode):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            self.rightBoundaryWithoutLeave(node.right)
        else:
            self.rightBoundaryWithoutLeave(node.left)
        self.res.append(node.val)

    def leaves(self, node: TreeNode):
        if not node:
            return
        if not node.left and not node.right:
            self.res.append(node.val)
            return
        self.leaves(node.left)
        self.leaves(node.right)

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.res.append(root.val)
        self.leftBoundaryWithoutLeave(root.left)  # question's description: if no root.left, left boundary is empty
        self.leaves(root.left)  # avoid root only case
        self.leaves(root.right)
        self.rightBoundaryWithoutLeave(root.right)
        return self.res
