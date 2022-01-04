# 2 stacks one is monotonic.
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min_stk) == 0 or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        t = self.stk.pop()
        if self.min_stk[-1] == t:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
