from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# hash map of {Node:new Node}
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nmap = {}
        curr, dummy = head, Node(-1)
        prev = dummy
        while curr:
            nmap[curr] = Node(curr.val)
            prev.next = nmap[curr]
            curr = curr.next
            prev = prev.next
        curr = head
        while curr:
            if curr.random:
                nmap[curr].random = nmap[curr.random]
            curr = curr.next
        return dummy.next
