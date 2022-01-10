from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# handle it like a tree. preorder dfs
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = None

        def preOrder(curr: Node):
            nonlocal prev
            if not curr:
                return
            c, n = curr.child, curr.next  # record next nodes for edges will change then
            if prev:
                prev.child = None
                prev.next = curr
                curr.prev = prev
            prev = curr
            preOrder(c)
            preOrder(n)

        preOrder(head)
        return head
