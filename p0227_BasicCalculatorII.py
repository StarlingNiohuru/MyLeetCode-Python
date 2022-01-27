# stack. calculate with temp digits and leading sign when meeting a new operator
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        temp = 0
        sign = "+"
        s += "+"
        for c in s:
            if c.isdigit():
                temp = temp * 10 + int(c)
            elif not c.isspace():
                if sign == "+":
                    stk.append(temp)
                elif sign == "-":
                    stk.append(-temp)
                elif sign == "*":
                    stk[-1] *= temp
                elif sign == "/":
                    stk[-1] = int(stk[-1] / temp)
                sign = c
                temp = 0
        res = sum(stk)
        return res
