class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for s in path.split('/'):
            if s:
                if s == '..':
                    if stk:
                        stk.pop()
                elif s != '.':
                    stk.append(s)
        res = "/" + "/".join(stk)
        return res
