from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS and global index
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        index = 0

        def inOrder():
            nonlocal index, s
            if index == len(s):
                return
            if s[index] == ')':
                index += 1
                return
            j = index + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            curr = TreeNode(int(s[index:j]))
            index = j
            if index < len(s) and s[index] == '(':
                index += 1
                curr.left = inOrder()
            if index < len(s) and s[index] == '(':
                index += 1
                curr.right = inOrder()
            index += 1
            return curr

        return inOrder()
