from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.s = 0

    def next(self, val: int) -> float:
        self.s += val
        self.q.append(val)
        if len(self.q) > self.size:
            self.s -= self.q.popleft()
        return self.s / len(self.q)
