class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if len(stk) > 0 and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        res = "".join(stk)
        return res
