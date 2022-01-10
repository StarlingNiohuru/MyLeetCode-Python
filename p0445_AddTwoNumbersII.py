from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        res = None
        i, carry = 0, 0
        while i < len(n1) or i < len(n2) or carry > 0:
            d1 = n1[-i - 1] if i < len(n1) else 0
            d2 = n2[-i - 1] if i < len(n2) else 0
            temp = d1 + d2 + carry
            carry = temp // 10
            ln = ListNode(temp % 10)
            ln.next = res
            res = ln
            i += 1
        return res
