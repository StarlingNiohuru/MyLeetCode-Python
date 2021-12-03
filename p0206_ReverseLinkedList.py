from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, cons = None, head, None
        while curr:
            cons = curr.next
            curr.next = prev
            prev = curr
            curr = cons
        return prev
