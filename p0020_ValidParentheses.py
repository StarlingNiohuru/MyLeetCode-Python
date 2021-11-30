class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        cmap = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stk.append(cmap[s[i]])
            else:
                if stk and stk[-1] == s[i]:
                    stk.pop()
                else:
                    return False
        return stk == []
