from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 4 kinds of cases. 1: curr<=interval<=next; 2: curr>=next and interval>=curr or interval<=next;
# 3: all the nodes are equal; 4: empty.
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            curr = Node(val=insertVal)
            curr.next = curr
            return curr
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break
            elif curr.val > curr.next.val and (curr.val <= insertVal or insertVal <= curr.next.val):
                break
            elif curr.val == head.val and curr.next == head:
                break
            else:
                curr = curr.next
        temp = Node(val=insertVal)
        temp.next = curr.next
        curr.next = temp
        return head
