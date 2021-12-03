class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ']':
                sub_str = ""
                while stk[-1].isalpha():
                    sub_str += stk[-1]
                    stk.pop()
                stk.pop()
                sub_str = sub_str[::-1]
                sub_digit = ""
                while stk and stk[-1].isdigit():
                    sub_digit += stk[-1]
                    stk.pop()
                sub_digit = int(sub_digit[::-1])
                for c1 in sub_str * sub_digit:
                    stk.append(c1)
            else:
                stk.append(c)
        res = "".join(stk)
        return res
