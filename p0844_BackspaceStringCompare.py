class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        for c in s:
            if c != '#':
                s1.append(c)
            elif s1:
                s1.pop()
        for c in t:
            if c != '#':
                s2.append(c)
            elif s2:
                s2.pop()
        return s1 == s2
