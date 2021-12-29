class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# find intersection of 2 linked lists
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        c1, c2 = p, q
        while c1 != c2:
            c1 = c1.parent if c1.parent else q
            c2 = c2.parent if c2.parent else p
        return c1
