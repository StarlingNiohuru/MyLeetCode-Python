class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


# linkedList.Choose a large prime 2069 as the number of bucket
class MyHashMap:

    def __init__(self):
        self.BASE = 2069
        self.buckets = [ListNode(-1, -1) for _ in range(self.BASE)]

    def put(self, key: int, value: int) -> None:
        mod = key % self.BASE
        curr, prev = self.buckets[mod], None
        while curr:
            if curr.key == key:
                curr.val = value
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        mod = key % self.BASE
        curr = self.buckets[mod]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        mod = key % self.BASE
        curr, prev, cons = self.buckets[mod], None, None
        while curr:
            cons = curr.next
            if curr.key == key:
                prev.next = cons
                curr.next = None
                return
            prev = curr
            curr = cons
