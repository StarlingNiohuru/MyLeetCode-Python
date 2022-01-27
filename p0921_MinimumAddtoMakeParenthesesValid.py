# stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for c in s:
            if c == "(":
                stk.append(c)
            elif len(stk) > 0 and stk[-1] == "(":
                stk.pop()
            else:
                stk.append(c)
        res = len(stk)
        return res
