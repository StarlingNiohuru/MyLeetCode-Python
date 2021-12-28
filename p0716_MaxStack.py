# 2 stacks one is monotonic.
class MaxStack:

    def __init__(self):
        self.stk = []
        self.max_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if len(self.max_stk) == 0 or x >= self.max_stk[-1]:
            self.max_stk.append(x)

    def pop(self) -> int:
        t = self.stk.pop()
        if self.max_stk[-1] == t:
            self.max_stk.pop()
        return t

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.max_stk[-1]

    def popMax(self) -> int:
        temp = []
        t = self.max_stk.pop()
        while self.stk[-1] != t:
            temp.append(self.stk.pop())
        self.stk.pop()
        while len(temp):
            self.push(temp.pop())  # don't forget recover max_stack
        return t
