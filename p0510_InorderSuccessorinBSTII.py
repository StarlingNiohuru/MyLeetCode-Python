from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# BST. leftmost of the right subtree or the first ancestor > node
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            curr = node.parent
            while curr and curr.val < node.val:
                curr = curr.parent
            return curr
