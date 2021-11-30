from collections import OrderedDict


# OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        res = -1
        if key in self.map:
            res = self.map[key]
            self.map.move_to_end(key)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.move_to_end(key)
        self.map[key] = value
        if len(self.map) > self.capacity:
            self.map.popitem(last=False)
