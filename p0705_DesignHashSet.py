class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# linkedList.Choose a large prime 2069 as the number of bucket
class MyHashSet:

    def __init__(self):
        self.BASE = 2069
        self.buckets = [ListNode(-1) for _ in range(self.BASE)]

    def add(self, key: int) -> None:
        mod = key % self.BASE
        curr, prev = self.buckets[mod], None
        while curr:
            if curr.val == key:
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        mod = key % self.BASE
        curr, prev, cons = self.buckets[mod], self.buckets[mod], None
        while curr:
            cons = curr.next
            if curr.val == key:
                prev.next = cons
                return
            prev = curr
            curr = cons

    def contains(self, key: int) -> bool:
        mod = key % self.BASE
        curr = self.buckets[mod]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
