class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if stk:
                    stk.pop()
                else:
                    remove.add(i)
        for i in stk:
            remove.add(i)
        res = ""
        for i in range(len(s)):
            if i not in remove:
                res += s[i]
        return res
