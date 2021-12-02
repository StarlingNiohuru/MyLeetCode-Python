import random


# map with index and list. mind duplicate case when replacing list
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            old_index, new_val = self.map[val], self.list[-1]
            self.list[old_index] = new_val
            self.list.pop()
            self.map[new_val] = old_index  # this line must come first in case of old index == new index
            self.map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
