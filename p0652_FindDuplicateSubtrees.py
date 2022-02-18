from collections import defaultdict
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS and hash map of serialize key the node
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        res = []

        def serialize(node: Optional[TreeNode]):
            nonlocal count, res
            if not node:
                return ""
            key = "(" + serialize(node.left) + str(node.val) + serialize(node.right) + ")"
            count[key] += 1
            if count[key] == 2:
                res.append(node)
            return key

        serialize(root)
        return res
