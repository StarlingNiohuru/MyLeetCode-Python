from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = None

    def dfs(self, node: TreeNode, target: int, path: List[int]):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == target:
            self.res.append(path.copy())
        else:
            self.dfs(node.left, target - node.val, path)
            self.dfs(node.right, target - node.val, path)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res
