from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# global prev + in order traverse
class Solution:
    prev = None

    def inOrder(self, node: Node):
        if not node:
            return
        self.inOrder(node.left)
        self.prev.right = node
        node.left = self.prev
        self.prev = node
        self.inOrder(node.right)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.prev = dummy = Node(-1)
        self.inOrder(root)
        first, last = dummy.right, self.prev
        if first and last:
            last.right = first
            first.left = last
        return first
