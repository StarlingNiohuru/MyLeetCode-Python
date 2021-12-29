from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in order iterative
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stk = []

    def next(self) -> int:
        while self.curr:
            self.stk.append(self.curr)
            self.curr = self.curr.left
        self.curr = self.stk.pop()
        res = self.curr.val
        self.curr = self.curr.right
        return res

    def hasNext(self) -> bool:
        return self.curr or len(self.stk) > 0
